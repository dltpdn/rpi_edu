import com.pi4j.io.gpio.*;

public class LED_Pi4j{
    public static void main(String[] args) throws InterruptedException {
        final GpioController gpio = GpioFactory.getInstance();
        final GpioPinDigitalOutput pin = 
                gpio.provisionDigitalOutputPin(RaspiPin.GPIO_01, "MyLED", PinState.HIGH);
        pin.setShutdownOptions(true, PinState.LOW);
        for(int i=0; i<5; i++){
        	pin.high();
	        System.out.println("Led : ON");
	        Thread.sleep(500);
	        pin.low();
	        System.out.println("Led : OFF");
	        Thread.sleep(500);
        }
        System.out.println("Exiting ControlGpioExample");
    }
}