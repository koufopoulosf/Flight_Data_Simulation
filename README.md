# Flight Data Simulation 🛩️

### Features:
- Simulates flight data of planes racing from the USA to Europe.
- Real-time visualization of plane positions on an interactive map.
- Demonstrates data generation, persistence, API creation, and mapping techniques.
- Uses a combination of Python, PostgreSQL, and JavaScript technologies.
- Nginx reverse proxy and docker setup for production deployment.
- Flexible and extensible for future data engineering projects.

### Moreover:
- 🏠 **On-Premise Capabilities:** Customized mapping implementation is possible for avoiding FOSS licensure conflicts.
- 🚀 **Expanding Beyond Flight Data:** We can effortlessly visualize any geospatial dataset, offering endless possibilities, including:
  
    - **Incident Reporting and Visualization:** Monitor and visualize incidents of interest, like car accidents or environmental events, providing a clear overview of occurrences and patterns.
    - **IoT Device Monitoring:** Extend the system to oversee installed IoT devices, showcasing real-time statuses and locations, enabling effective management and control.
    - **Supply Chain Tracking:** Track shipments, goods, and materials across the supply chain, enhancing transparency and optimizing logistics.
    - **Natural Disaster Assessment**: Rapidly assess and respond to natural disasters by visualizing affected areas and coordinating rescue efforts.

## Getting Started
```sh
apt update && apt upgrade -y
apt install docker.io docker-compose -y
git clone https://github.com/koufopoulosf/Flight_Data_Simulation && cd Flight_Data_Simulation
docker-compose up --build
```

### Made with ❤️ by Filippos