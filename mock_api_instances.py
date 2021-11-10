from jira_api import Sprint, Ticket


sprint_instance = Sprint(
    number=79,
    tickets=[
        Ticket(
            jira_id='W3D-3133',
            epic_name='Barrios',
            summary='[BE] Crear tipo de proyecto "Barrio"',
            status='In Progress',
            person_in_charge='Facundo Moreyra'
        ),
        Ticket(
            jira_id='W3D-3138',
            epic_name='Barrios',
            summary='[BE] Crear blacklist en lista de proyectos a publicar, incluir a dicha blacklist a los proyectos de tipo Barrio ',
            status='In Progress',
            person_in_charge='Facundo Moreyra'
        ),
        Ticket(
            jira_id='W3D-2764',
            epic_name='Filtración de Datos',
            summary='[BE] PoC private Uploads',
            status='MR',
            person_in_charge='Facundo Moreyra'
        ),
        Ticket(
            jira_id='W3D-3112',
            epic_name='Filtración de Datos',
            summary='[BE] Charla de Diseño de Upload custom',
            status='To Do',
            person_in_charge='Facundo Moreyra'
        ),
        Ticket(
            jira_id='W3D-1934',
            epic_name='Multitorre',
            summary='[FE] Actualizar router: rutas van a cambiar',
            status='In Progress',
            person_in_charge='Ignacio Guerra'
        ),
        Ticket(
            jira_id='W3D-3068',
            epic_name='Multitorre',
            summary='[FE] hint de botones de flecha de giro',
            status='To Do',
            person_in_charge='Franco Colares'
        ),
        Ticket(
            jira_id='W3D-3069',
            epic_name='Multitorre',
            summary='[FE] remover icono indicador de 360 en imagen de preview de unidad',
            status='To Do',
            person_in_charge='Franco Colares'
        ),
        Ticket(
            jira_id='W3D-3070',
            epic_name='Multitorre',
            summary='[FE] [DESKTOP] barra lateral debe estar abierta por default',
            status='To Do',
            person_in_charge='Franco Colares'
        ),
        Ticket(
            jira_id='W3D-3076',
            epic_name='Multitorre',
            summary='[TEAM] charla de revision de modelo “cluster” y como incluir popups informativos + detalles',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3116',
            epic_name='Multitorre',
            summary='[FE] Crear componentes básicos para las nuevas vistas de MT',
            status='To Do',
            person_in_charge='Ignacio Guerra'
        ),
        Ticket(
            jira_id='W3D-3121',
            epic_name='Multitorre',
            summary='[ADM] Prueba funcional - Carga, validación y publicación de proyecto completo en Staging (single torre)',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3149',
            epic_name='Multitorre',
            summary='[FE] actualizar links de acceso a las torres',
            status='To Do',
            person_in_charge='Franco Colares'
        ),
        Ticket(
            jira_id='W3D-3124',
            epic_name='Otros',
            summary='[TEAM] definir formulario de reporte de fallo',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3126',
            epic_name='Otros',
            summary='[TEAM] prefetch',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3127',
            epic_name='Otros',
            summary='[TEAM] Validacion + review',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3128',
            epic_name='Otros',
            summary='[TEAM] Showcase',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3129',
            epic_name='Otros',
            summary='[TEAM] Preparar demo | cierre de sprint',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3130',
            epic_name='Otros',
            summary='[TEAM] buffer estimaciones',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3131',
            epic_name='Otros',
            summary='[ADM] deploy modal',
            status='To Do',
            person_in_charge='TEAM'
        ),
        Ticket(
            jira_id='W3D-3144',
            epic_name='Otros',
            summary='[FE] Quitar Portal de las dependencias del proyecto',
            status='In Progress',
            person_in_charge='Franco Colares'
        ),
        Ticket(
            jira_id='W3D-3148',
            epic_name='Otros',
            summary='[FE] Implementar unitId / unitLabel en lugar de unitSlug',
            status='To Do',
            person_in_charge='Ignacio Guerra'
        ),
        Ticket(
            jira_id='W3D-3150',
            epic_name='Otros',
            summary='[FE][TD] Mantenimiento de project.json y availability.json',
            status='To Do',
            person_in_charge='Ignacio Guerra'
        ),
        Ticket(
            jira_id='W3D-3151',
            epic_name='Otros',
            summary='[ADM] test modal',
            status='To Do',
            person_in_charge='TEAM'
        )
    ]
)


