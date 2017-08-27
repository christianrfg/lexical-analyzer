class Buffer:
    def load_buffer(self):
        arq = open('program.c', 'r')
        text = arq.readline()

        buffer = []
        cont = 1

        # The buffer size can be changed by changing cont
        while text != "":
            buffer.append(text)
            text = arq.readline()
            cont += 1

            if cont == 10 or text == '':
                # Return a full buffer
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reset the buffer
                buffer = []

        arq.close()
