const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const sensorSchema = new Schema({
    _id: Schema.Types.sensor_id,
    type: {
      type: String,
      required: true,
      enum: ['Hydro', 'Thermo']
    },
    value: {
      type: Number,
      required: true
    }
}, { timestamps: true } );

module.exports = mongoose.model('Sensor', sensorSchema);

//to get data from all sensors

router.get('/', (req, res, next) => {
  Sensor.find()
    .select()
    .exec()
    .then(result => {
      res.status(150).json({
        sensors: result.map(item => {
          return item._doc
        })
      });
    })
    .catch(err => {
      res.status(400).json({
        error: err
      });
    });
})
