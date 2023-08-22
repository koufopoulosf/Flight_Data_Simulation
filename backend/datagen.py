from dotenv import load_dotenv
import asyncio, asyncpg, random, os

class FlightDataSimulator:
    def __init__(self):
        self.planes = []

    def generate_plane(self, plane_id):
        latitude = random.uniform(35,72) # Europe's approximate latitude range
        longitude = random.uniform(-130,-70) # Longitude range across America
        step_size = random.uniform(0.1, 1.0)  # Vary the step size for each plane
        self.planes.append({'id':plane_id, 'lat':latitude, 'long':longitude, 'step_size': step_size})
    
    def update_plane_trajectory(self):
        for plane in self.planes:
            # Update longitude for a racing effect
            if plane['long'] > 45:  # Wrap around when reaching the right side of Europe
                plane['long'] = -130  # Reset longitude to the left side of America
            
            plane['long'] += plane['step_size']  # Move horizontally based on step size

    async def send_data_to_db(self, conn):
        while True:
            self.update_plane_trajectory()
            data = [(plane['id'], plane['lat'], plane['long']) for plane in self.planes]
            await self.update_data(conn, data)
            await asyncio.sleep(1) # Sending data every 1 second
    
    async def update_data(self, conn, data):
        async with conn.transaction():
            await conn.executemany(
                "INSERT INTO flight_data (id, lat, long) VALUES ($1, $2, $3) ON CONFLICT (id) DO UPDATE SET lat = EXCLUDED.lat, long = EXCLUDED.long",
                data
            )

async def main():
    load_dotenv()
    dsn = "postgresql://"+os.getenv("pg_user")+":"+os.getenv("pg_password")+"@"+os.getenv("pg_host")+"/"+os.getenv("pg_database")
    async with asyncpg.create_pool(dsn=dsn) as pool:
        async with pool.acquire() as conn:
            simulator = FlightDataSimulator()
            for plane_id in range(1,51):
                simulator.generate_plane(plane_id)
            
            tasks = [
                asyncio.create_task(simulator.send_data_to_db(conn))
            ]
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())