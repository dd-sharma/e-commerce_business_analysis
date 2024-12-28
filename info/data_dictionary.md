# Data Dictionary

| **Variable Name** | **Description**                                                                                                           | **Data Type**       |
|--------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------|
| **InvoiceNo**      | Invoice number. A 6-digit integral number uniquely assigned to each transaction. If this code starts with the letter 'C', it indicates a cancellation. | Nominal             |
| **StockCode**      | Product (item) code. A 5-character code uniquely assigned to each distinct product.                                       | Nominal             |
| **Description**    | Product (item) name.                                                                                                     | Nominal             |
| **Quantity**       | The quantities of each product per transaction. Includes positive values (purchases) and negative values (returns).       | Numeric (integer)   |
| **UnitPrice**      | Unit price of the product per unit in sterling. Represents the price of a single product unit in GBP.                     | Numeric (float)     |
| **CustomerID**     | Customer number. A 5-digit integral number uniquely assigned to each customer. May contain null values for some transactions. | Nominal             |
| **Country**        | Name of the country where the customer resides. Reflects the geographic distribution of customers.                        | Nominal             |
| **InvoiceDate**    | Invoice date and time when the transaction was generated.                                                                | Numeric (datetime)  |

