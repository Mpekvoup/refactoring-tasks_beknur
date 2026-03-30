public abstract class ReportHandler {
    protected ReportHandler nextHandler;

    public ReportHandler setNext(ReportHandler handler) {
        this.nextHandler = handler;
        return handler;
    }

    public void handle(String report, String recipient) {
        process(report, recipient);
        if (nextHandler != null) {
            nextHandler.handle(report, recipient);
        }
    }

    protected abstract void process(String report, String recipient);
}
