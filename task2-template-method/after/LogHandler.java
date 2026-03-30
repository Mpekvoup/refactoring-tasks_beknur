public class LogHandler extends ReportHandler {
    private Logger logger;

    public LogHandler(Logger logger) {
        this.logger = logger;
    }

    @Override
    protected void process(String report, String recipient) {
        logger.info("Report generated for " + recipient);
    }
}
