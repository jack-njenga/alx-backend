import redis from "redis";

const client = redis.createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`);
});

function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.GET(schoolName, (err, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');