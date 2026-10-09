from narad_system.schema.yaml_order import order_document_components


def test_serialized_components_put_identity_before_parameter_groups() -> None:
    document = {
        "facility": {
            "components": [
                {
                    "ReferenceP": {"id": "inst:BEGIN/ReferenceP"},
                    "TwissP": {"id": "inst:BEGIN/TwissP"},
                    "id": "inst:BEGIN",
                    "kind": "BeginningEle",
                    "native_types": ["BeginningEle"],
                    "functions": ["Mark"],
                    "beamline_relation": "Inline",
                    "alias": ["start"],
                }
            ]
        }
    }

    component = order_document_components(document)["facility"]["components"][0]

    assert list(component) == [
        "id",
        "kind",
        "native_types",
        "functions",
        "beamline_relation",
        "alias",
        "ReferenceP",
        "TwissP",
    ]
