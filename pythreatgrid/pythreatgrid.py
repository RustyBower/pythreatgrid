#!/usr/bin/env python3
import requests


class ThreatGrid(object):
    def __init__(self, api_host, api_key, filename=None, vm=None, private=False, tags=[], playbook=None,
                 network_exit=None):
        # TODO - Fix potential issue if user passes / as the last character in the api host
        self.api_host = api_host
        self.api_key = api_key
        self.filename = filename
        self.vm = vm
        self.private = private
        self.tags = tags
        self.playbook = playbook
        self.network_exit = network_exit

    def submit_sample(self, sample):
        # Define required variables
        data = {
            'api_key': self.api_key,
        }

        # Define optional variables if they exist
        if self.filename:
            data['filename'] = self.filename
        if self.vm:
            data['vm'] = self.vm
        if self.private:
            data['private'] = self.private
        if self.tags:
            data['tags'] = self.tags
        if self.playbook:
            data['playbook'] = self.playbook
        if self.network_exit:
            data['network_exit'] = self.network_exit

        files = {
            'sample': sample
        }

        r = requests.post(url='%s/%s' % (self.api_host, 'samples'), files=files, data=data)
        return r.json()

    def make_get_request(self, uri):
        data = {
            'api_key': self.api_key,
        }

        r = requests.get(uri, data=data)
        return r.json()

    def get_samples_id_state(self, sample_id):
        # GET /samples/ID/state
        # ID	The sample ID
        # api_key	A secret token identifying the user and providing authentication
        # A JSON response with a state string as the data.
        return self.make_get_request('%s/samples/%s/state' % (self.api_host, sample_id))

    def get_samples_id_video(self, sample_id):
        # GET /samples/ID/video.webm
        # Requests the samples display output, transcoded to WEBM format. May
        # only be used with samples with a state of “succ”. Future revisions may
        # provide support for “fail” samples. This returns the WEBM stream, as
        # video/webm content-type.
        return self.make_get_request('%s/samples/%s/video.webm' % (self.api_host, sample_id))

    def get_samples_id_analysis(self, sample_id):
        # GET /samples/ID/analysis.json
        # The analysis.json file is a single JSON object which contains a
        # detailed overview of dynamic and static analysis results for the
        # sample.
        return self.make_get_request('%s/samples/%s/analysis.json' % (self.api_host, sample_id))

    def get_samples_id_processes(self, sample_id):
        # GET /samples/ID/processes.json
        # The processes.json file is a single JSON object which contains a
        # timeline of all process activity as determined by the dynamic analysis
        # engine.
        r = requests.get(url='%s/samples/%s/processes.json' % (self.api_host, sample_id))
        return r.json()

    # TODO - Determine if there's a better way to return this file to the user
    def get_samples_id_network(self, sample_id):
        # GET /samples/ID/network.pcap
        # The network.pcap is a tcpdump PCAP file, with all the network
        # activity of the sample.
        r = requests.get(url='%s/samples/%s/network.json' % (self.api_host, sample_id))
        return r.content

    # TODO - Determine if there's a better way to return this file to the user
    def get_samples_id_network_artifacts(self, sample_id):
        # GET /samples/ID/network-artifacts.zip
        # Zip archive containing artifacts extracted from the PCAP, the
        # network and annotations.network sections of analysis.json,
        # metadata containing more details about the extracted artifacts, and
        # SHA256->filename mappings for the artifacts. Related:
        # /samples/ID/extracted-artifacts.zip
        # for artifacts extracted from the sample itself during analysis.
        r = requests.get(url='%s/samples/%s/network-artifacts.zip' % (self.api_host, sample_id))
        return r.content

    def get_samples_id_warnings(self, sample_id):
        # GET samples/ID/warnings.json
        # The warnings.json file is a JSON structure describing any warnings that occured
        # during the analysis.
        return self.make_get_request('%s/samples/%s/warnings.json' % (self.api_host, sample_id))

    def get_samples_id_summary(self, sample_id):
        # GET /samples/ID/summary
        # Returns summary analysis information.
        # TODO - Determine if this is JSON
        return self.make_get_request('%s/samples/%s/summary' % (self.api_host, sample_id))

    def get_samples_id_threat(self, sample_id):
        # GET /samples/ID/threat
        # Returns a summary of the threats detected during analysis.
        # TODO - Determine if this is JSON
        return self.make_get_request('%s/samples/%s/threat' % (self.api_host, sample_id))

    def get_samples_id_report(self, sample_id):
        # GET /samples/ID/report.html
        # The report.html file is a stand-alone, complete report on the sample
        # run. It is designed to be emailed or printed.
        r = requests.get(url='%s/samples/%s/report.html' % (self.api_host, sample_id))
        return r.text

    def get_samples_id_sample(self, sample_id):
        # GET /samples/ID/sample.zip
        # The sample.zip file is an archive of the sample itself, in a zip
        # format to as a form of quarantine.
        r = requests.get(url='%s/samples/%s/sample.zip' % (self.api_host, sample_id))
        return r.content

    def get_samples_id_screenshot(self, sample_id):
        # GET /samples/ID/screenshot.png
        # The screenshot.png file is a screenshot of the sample. These
        # screenshots are displayed at the top of the Mask dashboard in the
        # Recent Samples component. They can also be downloaded.
        r = requests.get(url='%s/samples/%s/screenshot.png' % (self.api_host, sample_id))
        return r.content

    def get_samples_id_extracted_artifacts(self, sample_id):
        # GET /samples/ID/extracted-artifacts.zip
        # Zip archive containing artifacts extracted from the sample during
        # analysis. Artifacts with an Origin of “extracted” in the artifacts
        # section of the sample’s analysis.json are found in this
        # archive. Related:
        # /samples/ID/network-artifacts.zip
        # for artifacts extracted from the PCAP.
        r = requests.get(url='%s/samples/%s/extracted-artifacts.zip' % (self.api_host, sample_id))
        return r.content

    def get_samples_id_analysis_iocs(self, sample_id):
        # GET /samples/ID/analysis/iocs/IOC
        # Returns a JSON list of the Indicators of Compromise identified in
        # this sample run.
        return self.make_get_request('%s/samples/%s/analysis/iocs' % (self.api_host, sample_id))

    def get_samples_id_analysis_iocs_ioc(self, sample_id, ioc):
        # GET /samples/ID/analysis/iocs
        # Returns a JSON list of the Indicators of Compromise identified in
        # this sample run.
        # TODO - Check if this is JSON
        return self.make_get_request('%s/samples/%s/analysis/iocs/%s' % (self.api_host, sample_id, ioc))

    def get_samples_id_analysis_network_streams(self, sample_id):
        # GET /samples/ID/analysis/network_streams
        # Returns a JSON object whose attributes are Network Stream IDs,
        # sequential numeric identifiers of network sessions. It will include
        # data about any decoded protocols within the session, such as HTTP, IRC
        # and DNS traffic.
        return self.make_get_request('%s/samples/%s/analysis/network_streams' % (self.api_host, sample_id))

    def get_samples_id_analysis_network_streams_nsid(self, sample_id, nsid):
        # GET /samples/ID/analysis/network_streams/NSID
        # Returns the JSON object describing the specified Network Stream.
        return self.make_get_request('%s/samples/%s/analysis/network_streams/%s' % (self.api_host, sample_id, nsid))

    def get_samples_id_analysis_artifacts(self, sample_id):
        # GET /samples/ID/analysis/artifacts
        # Returns a JSON object whose attributes are Artifact IDs, sequential
        # numeric identifiers of artifact produced by the sample. These can be
        # from the disk, network, or memory.
        return self.make_get_request('%s/samples/%s/analysis/artifacts' % (self.api_host, sample_id))

    def get_samples_id_analysis_artifacts_aid(self, sample_id, aid):
        # GET /samples/ID/analysis/artifacts
        # Returns a JSON object, which is a summary of the static analysis of this artifact.
        return self.make_get_request('%s/samples/%s/analysis/artifacts/%s' % (self.api_host, sample_id, aid))

    def get_samples_id_analysis_processes(self, sample_id):
        # GET /samples/ID/analysis/processes
        # Returns a JSON object whose attributes are PIDs, and whose values are
        # process summaries.
        return self.make_get_request('%s/samples/%s/analysis/processes' % (self.api_host, sample_id))

    def get_samples_id_analysis_processes_pid(self, sample_id, pid):
        # GET /samples/ID/analysis/processes/PID
        # Returns a JSON object, which is the process summary of the specified PID.
        r = requests.get(url='%s/samples/%s/analysis/processes/%s' % (self.api_host, sample_id, pid))
        return r.json()

    def get_samples_id_analysis_annotations(self, sample_id):
        # GET /samples/ID/analysis/annotations
        # Returns a JSON object, representing the annotation information in the report.
        return self.make_get_request('%s/samples/%s/analysis/annotations' % (self.api_host, sample_id))

    def get_samples_id_analysis_metadata(self, sample_id):
        # GET /samples/ID/analysis/metadata
        # Returns a JSON object, representing the metadata information in the report.
        return self.make_get_request('%s/samples/%s/analysis/metadata' % (self.api_host, sample_id))
