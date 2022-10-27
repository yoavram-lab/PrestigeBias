from PyPDF2 import PdfFileMerger


def merge(thesis_path, hebrew_cover):
    merger = PdfFileMerger()

    thesis_file = open(thesis_path, "rb")
    hebrew_file = open(hebrew_cover, "rb")

    # add all pages of thesis to output
    merger.append(fileobj=thesis_file)

    # append hebrew cover to the end of the output document
    merger.append(hebrew_file)

    # Write to an output PDF document
    output = open(output_path(thesis_path), "wb")
    merger.write(output)


def output_path(thesis_path: str):
    assert thesis_path.endswith('.pdf')
    return thesis_path[:-4] + '_with_hebrew_abstract' + '.pdf'


if __name__ == '__main__':
    merge('ms.pdf', 'HebrewThesisSaar.pdf')