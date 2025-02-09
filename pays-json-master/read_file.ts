import { PAYS } from './All_countries.ts'

// Initialize empty arrays for countries and capitals
let countries: string[] = [];
let capitals: string[] = [];

// Iterate over each entry in the PAYS array
PAYS.forEach(countryInfo => {
    // Extract country name and capital
    let countryName: string = countryInfo.name;
    let capital: string = countryInfo.capital;

    // Add country name and capital to the respective arrays
    countries.push(countryName);
    capitals.push(capital);
});

// Print the arrays (optional)
console.log("Countries:", countries);
console.log("Capitals:", capitals);