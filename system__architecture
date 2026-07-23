# System Architecture

## Introduction

System architecture explains how computer hardware, software, and networking components work together to perform tasks. Every action we perform on a computer, such as opening a browser or saving a file, goes through several layers before the result is displayed back on the screen.

---

# The OSI Model

The OSI (Open Systems Interconnection) model is a conceptual framework that explains how computers communicate over a network. It divides network communication into seven different layers, with each layer performing a specific function.

## The Seven Layers of the OSI Model

### 7. Application Layer
This is the layer closest to the user. It provides network services to applications like web browsers, email clients, and messaging apps.

### 6. Presentation Layer
This layer is responsible for formatting, encrypting, and compressing data before it is sent across the network.

### 5. Session Layer
The session layer establishes, manages, and terminates communication sessions between two devices.

### 4. Transport Layer
This layer ensures reliable delivery of data between devices.

### 3. Network Layer
The network layer determines the best route for data to travel across networks.

### 2. Data Link Layer
This layer transfers data between devices on the same network.

### 1. Physical Layer
This is the lowest layer. It handles the transmission of raw bits over physical media.

![OSI](osi-1.webp)

# Why the OSI Model Is Not Used in Real-World Production
Although the OSI model is useful for learning networking concepts, it is rarely implemented exactly as designed in production systems.

The OSI model remains valuable because it helps engineers troubleshoot network problems by separating communication into logical layers.

# The Model Used in the Real World  is the TCP/IP

The TCP/IP Model is the networking model actually used on the Internet.

It is simpler and directly matches the protocols used in modern networks.

## TCP/IP Layers

### 4. Application Layer
Combines the OSI Application, Presentation, and Session layers.

### 3. Transport Layer
Responsible for communication between applications.

### 2. Internet Layer
Equivalent to the OSI Network Layer.

### 1. Network Access Layer
Combines the OSI Data Link and Physical layers.

![TCP LAYERS](layers-1.jfif)

# What happens when you perform an action From GUI to the Kernel and Back
Whenever you perform an action on your computer, such as clicking a button to open a web browser, many components work together behind the scenes.

The process is as follows.
# What Happens When You Perform an Action (From GUI to the Kernel and Back)

### 1. Graphical User Interface (GUI)
The process starts when you perform an action like clicking an icon or pressing a key. The GUI detects your input and sends the information to the application. This is the part of the operating system that you interact with directly.

### 2. Application
The application receives the request from the GUI and determines what needs to be done. For example, if you click on a browser, the browser prepares to open. It then asks the operating system for permission to use system resources.

### 3. System Call
The application cannot communicate directly with the hardware. Instead, it sends a system call to the operating system. A system call is simply a request for the operating system to perform a task.

### 4. Kernel
The kernel receives the system call and decides how to handle it. It controls communication between the software and the computer's hardware. The kernel also makes sure that resources are shared safely between programs.

### 5. Process Management
The kernel creates or manages the process needed to complete the task. It schedules the process so the CPU knows when to execute it. This allows multiple programs to run without interfering with one another.

### 6. Memory Management
The operating system allocates enough memory (RAM) for the application to run. It keeps each program in its own memory space to prevent conflicts. This helps improve both performance and security.

### 7. Address Translation
The Memory Management Unit (MMU) converts virtual memory addresses into physical memory addresses. This allows the CPU to locate the correct data in RAM. It also helps the operating system manage memory efficiently.

### 8. CPU Execution
The CPU begins processing the instructions needed to complete the task. It follows the Fetch, Decode, and Execute cycle for every instruction. These steps allow the CPU to carry out operations correctly.

### 9. Hardware Access
If the task requires hardware, the kernel communicates with the appropriate device driver. The driver controls hardware such as the hard drive, keyboard, printer, or network card. This ensures the hardware performs the requested operation.

### 10. Return Result
After the hardware or CPU finishes the task, the kernel collects the result. It sends the completed information back to the application. The application then prepares the output for the user.

### 11. GUI Updates
Finally, the application sends the result to the GUI. The GUI refreshes the screen and displays the completed action. For example, a program opens, a file appears, or a webpage loads successfully.
![ACTIONS PERFORMED](actions-1.png)

# Summary

Every action performed on a computer involves multiple layers of hardware and software working together. The GUI captures user input, the application requests services through system calls, the kernel manages hardware resources, memory and the CPU process instructions, and the results are returned to the application and displayed back to the user. Understanding these processes helps explain how operating systems and networks function efficiently.
