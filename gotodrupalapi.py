import sublime_plugin
import webbrowser

# -------------------------------------------
# { "keys": ["super+shift+a"], "command": "open_drupalapi" }
# -------------------------------------------


# Open the URL in the current selection
class GotoDrupalapiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            # if region.begin and region.begin are the same
            # no selection has been made, so grab the whole word
            if region.begin() == region.end():
                word = self.view.word(region)
            # otherwise, grab just the selection
            else:
                word = region
            if not word.empty():
                keyword = self.view.substr(word)
                webbrowser.open_new_tab("http://api.drupal.org/api/search/7/%s" % keyword)
