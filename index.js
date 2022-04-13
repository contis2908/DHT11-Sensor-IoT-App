
setInterval(() => {
    console.log(new Date(), ' -- Hello From Device:', process.env.DEVICE_NAME, 'Serial Number:', process.env.DEVICE_SERIAL_NUMBER);
}, 1000);
