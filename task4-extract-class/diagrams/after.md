# UML-диаграмма классов ПОСЛЕ рефакторинга

```mermaid
classDiagram
    class Employee {
        -id: String
        -firstName: String
        -lastName: String
        -birthDate: Date
        -email: String
        -phone: String
        -address: Address
        -bankDetails: BankDetails
        -salaryCalculator: SalaryCalculator
        +Employee(...)
        +getFullName(): String
        +getFullAddress(): String
        +calculateNetSalary(): double
        +formatForPayroll(): String
        +updateAddress(Address): void
        +updateBankDetails(BankDetails): void
        +updateSalary(double, double, double): void
        +getAddress(): Address
        +getBankDetails(): BankDetails
        +getSalaryCalculator(): SalaryCalculator
    }

    class Address {
        <<Value Object>>
        -streetAddress: String final
        -city: String final
        -zipCode: String final
        -country: String final
        +Address(...)
        +getFullAddress(): String
        +getStreetAddress(): String
        +getCity(): String
        +getZipCode(): String
        +getCountry(): String
        +toString(): String
        +equals(Object): boolean
        +hashCode(): int
    }

    class BankDetails {
        <<Value Object>>
        -bankName: String final
        -accountNumber: String final
        -routingNumber: String final
        +BankDetails(...)
        +validate(): boolean
        +getBankName(): String
        +getAccountNumber(): String
        +getRoutingNumber(): String
        +toString(): String
        +equals(Object): boolean
        +hashCode(): int
    }

    class SalaryCalculator {
        -baseSalary: double
        -overtimeHours: int
        -taxRate: double
        -pensionRate: double
        -healthInsuranceRate: double
        +SalaryCalculator(...)
        +calculateNetSalary(): double
        +calculateGrossSalary(): double
        +updateSalary(double, int, double, double, double): void
        +getBaseSalary(): double
        +getOvertimeHours(): int
        +getTaxRate(): double
        +getPensionRate(): double
        +getHealthInsuranceRate(): double
    }

    Employee --> Address
    Employee --> BankDetails
    Employee --> SalaryCalculator
```
