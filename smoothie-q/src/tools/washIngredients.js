
/**
 * parses a string to remove numbers, puncuation, all measurement types.
 * @param {String} `ingredient`
 * @return {String} `washedIngredient`
 */
const washIngredient = (ingredient) => {
    let washedIngredient = ingredient.replace(/[^A-za-z\s]/g, "").toLowerCase();

    const measurements = [
        'teaspoon', 'tablespoon', 'spoon', 'fork', 'cup', 'fluid', 'ounce', 'gill', 'pint',
        'quart', 'gallon', 'milliliter', 'millilitre', 'liter', 'litre', 'deciliter',
        'decilitre', 'pound', 'milligram', 'gram', 'chopped', 'diced', 'halved', 'pitted',
        'divided', 'broken', 'into', 'chunks', 'hulled', 'in', 'half', 'container', 'such',
        'as', 'uv',
    ]

    // add plurals
    measurements.forEach(measurement => {
        measurements.push(measurement + 's');
    })

    const expStr = measurements.join("|");
	washedIngredient = washedIngredient.replace(new RegExp('\\b(' + expStr + ')\\b', 'gi'), ' ')
                    .replace(/\s{2,}/g, ' ');

    return washedIngredient.trim();
}

export default washIngredient;