import java.util.Date;

/**
 * Класс сотрудника после рефакторинга.
 * Использует Value Objects для группировки связанных данных.
 * Соблюдает принцип Single Responsibility - отвечает только за личные данные.
 */
public class Employee {
    private String id;
    private String firstName;
    private String lastName;
    private Date birthDate;
    private String email;
    private String phone;

    // Агрегированные объекты
    private Address address;
    private BankDetails bankDetails;
    private SalaryCalculator salaryCalculator;

    /**
     * Конструктор сотрудника с агрегированными объектами.
     */
    public Employee(String id, String firstName, String lastName, Date birthDate,
                   String email, String phone,
                   Address address,
                   BankDetails bankDetails,
                   SalaryCalculator salaryCalculator) {
        if (id == null || firstName == null || lastName == null) {
            throw new IllegalArgumentException("Personal details must be non-null");
        }
        if (address == null || bankDetails == null || salaryCalculator == null) {
            throw new IllegalArgumentException("Address, bank details, and salary calculator must be non-null");
        }
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthDate = birthDate;
        this.email = email;
        this.phone = phone;
        this.address = address;
        this.bankDetails = bankDetails;
        this.salaryCalculator = salaryCalculator;
    }

    /**
     * Возвращает полное имя сотрудника.
     * @return полное имя
     */
    public String getFullName() {
        return firstName + " " + lastName;
    }

    /**
     * Делегирующий метод для получения полного адреса.
     * Соблюдает закон Деметры.
     * @return полный адрес
     */
    public String getFullAddress() {
        return address.getFullAddress();
    }

    /**
     * Делегирующий метод для расчета чистой зарплаты.
     * @return чистая зарплата
     */
    public double calculateNetSalary() {
        return salaryCalculator.calculateNetSalary();
    }

    /**
     * Форматирование для payroll системы.
     * @return строка для payroll
     */
    public String formatForPayroll() {
        return id + "|" + getFullName() + "|" + calculateNetSalary() + "|" +
               bankDetails.getBankName() + "|" + bankDetails.getAccountNumber();
    }

    /**
     * Обновление адреса (создание нового immutable объекта).
     * @param newAddress новый адрес
     */
    public void updateAddress(Address newAddress) {
        if (newAddress == null) {
            throw new IllegalArgumentException("Address cannot be null");
        }
        this.address = newAddress;
    }

    /**
     * Обновление банковских данных (создание нового immutable объекта).
     * @param newBankDetails новые банковские данные
     */
    public void updateBankDetails(BankDetails newBankDetails) {
        if (newBankDetails == null) {
            throw new IllegalArgumentException("Bank details cannot be null");
        }
        if (!newBankDetails.validate()) {
            throw new IllegalArgumentException("Invalid bank details");
        }
        this.bankDetails = newBankDetails;
    }

    /**
     * Обновление параметров зарплаты.
     * @param baseSalary новая базовая зарплата
     * @param overtimeHours новые часы сверхурочной работы
     * @param taxRate новая налоговая ставка
     * @param pensionRate новая ставка пенсионных отчислений
     * @param healthInsuranceRate новая ставка медицинского страхования
     */
    public void updateSalary(double baseSalary, int overtimeHours, double taxRate,
                            double pensionRate, double healthInsuranceRate) {
        salaryCalculator.updateSalary(baseSalary, overtimeHours, taxRate, pensionRate, healthInsuranceRate);
    }

    // Геттеры для личных данных
    public String getId() { return id; }
    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    public Date getBirthDate() { return birthDate; }
    public String getEmail() { return email; }
    public String getPhone() { return phone; }

    // Геттеры для агрегированных объектов
    public Address getAddress() { return address; }
    public BankDetails getBankDetails() { return bankDetails; }
    public SalaryCalculator getSalaryCalculator() { return salaryCalculator; }
}
