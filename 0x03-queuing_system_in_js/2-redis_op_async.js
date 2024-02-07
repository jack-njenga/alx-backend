import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err.toString()}`);
});
const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
    client.SET(schoolName, value, redis.print);
}

// function displaySchoolValue(schoolName) {
//     client.GET(schoolName, (err, reply) => {
//         console.log(reply);
//     });
// }
async function displaySchoolValue(schoolName) {
    try {
        const reply = await getAsync(schoolName);
        console.log(reply);
    }
    catch (err) {throw err;}
    }


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');