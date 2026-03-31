import java.util.Date;

public class Employee {
    private String id;
    private String firstName;
    private String lastName;
    private Date birthDate;
    private String email;
    private String phone;

    private String streetAddress;
    private String city;
    private String zipCode;
    private String country;

    private String bankName;
    private String accountNumber;
    private String routingNumber;

    private double baseSalary;
    private double bonus;
    private double taxRate;

    public Employee(String id, String firstName, String lastName, Date birthDate,
                   String email, String phone,
                   String streetAddress, String city, String zipCode, String country,
                   String bankName, String accountNumber, String routingNumber,
                   double baseSalary, double bonus, double taxRate) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthDate = birthDate;
        this.email = email;
        this.phone = phone;
        this.streetAddress = streetAddress;
        this.city = city;
        this.zipCode = zipCode;
        this.country = country;
        this.bankName = bankName;
        this.accountNumber = accountNumber;
        this.routingNumber = routingNumber;
        this.baseSalary = baseSalary;
        this.bonus = bonus;
        this.taxRate = taxRate;
    }

    public String getFullName() {
        return firstName + " " + lastName;
    }

    public String getFullAddress() {
        return streetAddress + ", " + city + ", " + zipCode + ", " + country;
    }

    public double calculateNetSalary() {
        double gross = baseSalary + bonus;
        double tax = gross * taxRate;
        return gross - tax;
    }

    public String getBankDetails() {
        return "Bank: " + bankName + ", Account: " + accountNumber + ", Routing: " + routingNumber;
    }

    public void updateAddress(String streetAddress, String city, String zipCode, String country) {
        this.streetAddress = streetAddress;
        this.city = city;
        this.zipCode = zipCode;
        this.country = country;
    }

    public void updateBankInfo(String bankName, String accountNumber, String routingNumber) {
        this.bankName = bankName;
        this.accountNumber = accountNumber;
        this.routingNumber = routingNumber;
    }

    public void updateSalary(double baseSalary, double bonus, double taxRate) {
        this.baseSalary = baseSalary;
        this.bonus = bonus;
        this.taxRate = taxRate;
    }

    public boolean validateBankAccount() {
        return accountNumber != null && accountNumber.length() >= 8 &&
               routingNumber != null && routingNumber.length() == 9;
    }

    public String formatForPayroll() {
        return id + "|" + getFullName() + "|" + calculateNetSalary() + "|" +
               bankName + "|" + accountNumber;
    }

    public String getId() { return id; }
    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    public Date getBirthDate() { return birthDate; }
    public String getEmail() { return email; }
    public String getPhone() { return phone; }
    public String getStreetAddress() { return streetAddress; }
    public String getCity() { return city; }
    public String getZipCode() { return zipCode; }
    public String getCountry() { return country; }
    public String getBankName() { return bankName; }
    public String getAccountNumber() { return accountNumber; }
    public String getRoutingNumber() { return routingNumber; }
    public double getBaseSalary() { return baseSalary; }
    public double getBonus() { return bonus; }
    public double getTaxRate() { return taxRate; }
}
