import java.io.FileWriter;
import java.io.IOException;
import java.util.Date;

public class ArchiveHandler extends ReportHandler {
    private String archivePath;

    public ArchiveHandler(String archivePath) {
        this.archivePath = archivePath;
    }

    @Override
    protected void process(String report, String recipient) {
        try {
            String filename = archivePath + "/" + recipient + "_" + new Date().getTime() + ".txt";
            FileWriter writer = new FileWriter(filename);
            writer.write(report);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
