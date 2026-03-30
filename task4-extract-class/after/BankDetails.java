import java.util.Objects;

/**
 * Value Object для банковских данных сотрудника.
 * Immutable класс - все поля final, без сеттеров.
 */
public final class BankDetails {
    private final String bankName;
    private final String accountNumber;
    private final String routingNumber;

    /**
     * Конструктор банковских данных.
     * @param bankName название банка
     * @param accountNumber номер счета
     * @param routingNumber routing номер (маршрутный код)
     */
    public BankDetails(String bankName, String accountNumber, String routingNumber) {
        if (bankName == null || accountNumber == null || routingNumber == null) {
            throw new IllegalArgumentException("All bank details must be non-null");
        }
        this.bankName = bankName;
        this.accountNumber = accountNumber;
        this.routingNumber = routingNumber;
    }

    /**
     * Валидация банковского счета.
     * @return true если счет валиден
     */
    public boolean validate() {
        return accountNumber.length() >= 8 && routingNumber.length() == 9;
    }

    public String getBankName() { return bankName; }
    public String getAccountNumber() { return accountNumber; }
    public String getRoutingNumber() { return routingNumber; }

    @Override
    public String toString() {
        return "Bank: " + bankName + ", Account: " + accountNumber + ", Routing: " + routingNumber;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        BankDetails that = (BankDetails) o;
        return Objects.equals(bankName, that.bankName) &&
               Objects.equals(accountNumber, that.accountNumber) &&
               Objects.equals(routingNumber, that.routingNumber);
    }

    @Override
    public int hashCode() {
        return Objects.hash(bankName, accountNumber, routingNumber);
    }
}
