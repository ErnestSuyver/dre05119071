function webp(stream, file, width) {
    return stream
        .clone()
        .webp({ quality: data.quality ? data.quality : 85 })
        .resize({ width: width })
        .toFile(`${data.inputDir}${data.imgDir}${file}-${width}.webp`)
        .then((sharpObj) => {
            sharpObj.file = `${data.inputDir}${data.imgDir}${file}-${width}.webp`;
            sharpObj.size = `${bytesToKB(sharpObj.size)} KB`;
            sharpObj.quality = data.quality ? data.quality : 85;
            data.debug ? console.log(sharpObj) : null;
        })
        .catch((err) => {
            console.log(`Error transforming ${data.inputDir}${data.imgDir}${data.src}`, err);
        })
};


toFile moet dus zijn toBuffer, bv zoiets?

function webp(stream, file, width) {
    return stream
      .clone()
      .webp({ quality: data.quality ? data.quality : 85, lossless: false })
      .resize({ width: width })
      .toBuffer({ resolveWithObject: true })
      .then(({ data, info }) => {
        const sharpObj = { ...info };
        sharpObj.file = `${data.inputDir}${data.imgDir}${file}-${width}.webp`;
        sharpObj.size = `${bytesToKB(data.length)} KB`;
        sharpObj.quality = data.quality ? data.quality : 85;
        data.debug ? console.log(sharpObj) : null;
        return sharpObj;
      })
      .catch((err) => {
        console.log(`Error transforming ${data.inputDir}${data.imgDir}${data.src}`, err);
      });
  };
  