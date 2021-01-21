import PySimpleGUI as sg

from cblaster.gui.parts import TextLabel


sg.theme("Lightgrey1")


extract_frame = sg.Frame(
    "Extract",
    layout=[
        [sg.Text(
            "This module will allow you to extract sequences from saved cblaster"
            " session files. You can filter sequences by the queries they hit,"
            " or the organisms and scaffolds they belong to. This module is designed"
            " to answer a question like: 'how can I get all of the methyltransferase"
            " sequences from homologous gene clusters in Aspergillus genomes?'",
            size=(60, 4)
        )],
        [sg.Text(
            "A session file (.json) generated by a cblaster search.",
            size=(60, 1)
        )],
        [TextLabel("Session file"),
         sg.InputText(size=(34, 1), key="extract_session"),
         sg.FileBrowse(key="extract_session")],

        [sg.Text(
            "File path to save the extracted sequences to."
            " If not provided, they will be printed to the terminal.",
            size=(60, 2)
        )],
        [TextLabel("Output file"),
         sg.InputText(key="extract_output", size=(34, 1)),
         sg.FileSaveAs(key="extract_output")],
        [sg.Text(
            "The names of query sequences which extracted sequences match."
            " You can provide multiple names here.",
            size=(60, 2)
        )],
        [TextLabel("Query sequences"), sg.InputText(key="queries")],

        [sg.Text(
            "Organisms that extracted sequences must be from. These take the form"
            " of regular expression patterns and are therefore quite flexible."
            " You can provide more than one pattern."
            " For example, to extract sequences only from Aspergillus and Penicillium"
            " genomes, you might specify: 'Aspergillus.*' 'Penicillium.*'"
            " See the user guide for more examples.",
            size=(60, 5)
        )],
        [TextLabel("Organisms"), sg.InputText(key="organisms")],

        [sg.Text(
            "Scaffolds that extracted sequences must be on. These can be scaffold"
            " names or names AND coordinate ranges. For example, you could specify"
            " scaffold_1, which would retrieve ALL clusters on scaffold_1, or"
            " scaffold_1:10000-50000, which would retrieve only those from position"
            " 10000 to 50000. This can be used to extract sequences from specific"
            " clusters.",
            size=(60, 5)
        )],
        [TextLabel("Scaffolds"), sg.InputText(key="scaffolds")],
        [sg.Text(
            "Generate delimited output instead of human readable.",
            size=(60, 1)
        )],
        [TextLabel("Delimiter"), sg.InputText(key="delimiter")],
        [sg.Text(
            "Download extracted sequences from NCBI and convert them to FASTA format.",
            size=(60, 1)
        )],
        [TextLabel("Download"), sg.Checkbox("", key="download", default=False)],
        [sg.Text(
            "Don't include source information in extracted sequence headers.",
            size=(60, 1)
        )],
        [TextLabel("Name only"), sg.Checkbox("", key="name_only", default=False)],

    ],
    title_color="blue",
    font="Arial 10 bold",
    relief="flat",
)

layout = [[extract_frame]]
