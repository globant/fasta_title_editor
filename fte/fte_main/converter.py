
from Bio import SeqIO

class Convert_fasta_header():
    ''' Convert '''
    def __init__(self, seq_file_in, seq_file_out, custom_label=''):
        ''' Read files into seq objects '''
        #self.fh = open(seq_file_in, "rU")
        self.fh = seq_file_in
        self.seqs = []
        self.fileout = seq_file_out
        self.cl = custom_label

    def conv_gro_sp(self):
        ''' genero_especie '''
        for record in SeqIO.parse(self.fh, "fasta"):
            self.code = record.description.split('|')[3].split('.')[0]
            self.name = record.description.split(' ')[1]
            self.name2 = record.description.split(' ')[2].split('.')[0]
            if self.cl:
                self.new_header = '_'.join([self.code, self.name, self.name2, self.cl])
            else:
                self.new_header = '_'.join([self.code, self.name, self.name2])
            record.description = ''
            record.id = self.new_header
            self.seqs.append(record)            
        self.fh.close()
        self._write()

    def conv_gsp(self):
        ''' gespecie '''
        for record in SeqIO.parse(self.fh, "fasta"):
            self.code = record.description.split('|')[3].split('.')[0]
            self.name = record.description.split(' ')[1][0]
            self.name2 = record.description.split(' ')[2].split('.')[0]
            if self.cl:
                self.new_header = '_'.join([self.code, self.name + self.name2, self.cl])
            else:
                self.new_header = '_'.join([self.code, self.name + self.name2])
            record.description = ''
            record.id = self.new_header
            self.seqs.append(record)            
        self.fh.close()
        self._write()

        
    def _write(self):
        self.fh = open(self.fileout, "w")
        SeqIO.write(self.seqs, self.fh, "fasta")
        self.fh.close() 

#c = Convert_fasta_header("input.txt",'out.txt', 'BuenosAires')
#c.conv_gro_sp()
#c.conv_gsp()

"""
from Bio import SeqIO
sequences = ... # add code here
output_handle = open("example.fasta", "w")
SeqIO.write(sequences, output_handle, "fasta")
output_handle.close()
"""

