kuberenets:

kubectl run -i --tty --rm debug --image=alpine --restart=Never -- sh

# Pull the Cosmos DB Emulator image
docker pull mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator

# Run the Cosmos DB Emulator container
docker run -d -p 8081:8081 -p 10251:10251 -p 10252:10252 -p 10253:10253 -p 10254:10254 -p 10255:10255 mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator
