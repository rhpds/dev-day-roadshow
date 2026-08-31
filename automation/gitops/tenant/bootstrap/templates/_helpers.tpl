{{- define "tenant-bootstrap.username" -}}
{{ .Values.tenant.username }}
{{- end -}}

{{- define "tenant-bootstrap.name" -}}
tenant-{{ .Values.tenant.username }}
{{- end -}}
