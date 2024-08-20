def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        # Calculate the discounted price
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return the original price
        return price

def main():
    # Prompt the user for the original price and discount percentage
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print the final price
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values for price and discount percentage.")

# Run the main function
if __name__ == "__main__":
    main()
