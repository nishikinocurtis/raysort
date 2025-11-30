# pylint: disable=use-dict-literal
import os

from raysort.config.common import (
    InstanceType,
    JobConfig,
    get_steps,
)

local_cluster = dict(
    # instance_count=min(os.cpu_count() or 16, 16),
    instance_count=4,
    instance_type=InstanceType(
        name="local",
        cpu=8,
        # memory_gib=0,  # not used
        memory_gib=1,  # not used
    ),
    local=False,
)

local_base_app_config = dict(
    **get_steps(),
    map_parallelism_multiplier=1,
    reduce_parallelism_multiplier=1,
)

local_mini_app_config = dict(
    **local_base_app_config,
    total_gb=0.16,
    input_part_gb=0.01,
)

local_app_config = dict(
    **local_base_app_config,
    total_gb=0.512,
    input_part_gb=0.002,
)

local_64gb_64par = dict(
    **local_base_app_config,
    total_gb=64,
    input_part_gb=1,
)

local_32gb_64par = dict(
    **local_base_app_config,
    total_gb=32,
    input_part_gb=0.5,
)

local_32gb_32par = dict(
    **local_base_app_config,
    total_gb=32,
    input_part_gb=1,
)

local_32gb_16par = dict(
    **local_base_app_config,
    total_gb=32,
    input_part_gb=2,
)

local_16gb_128par = dict(
    **local_base_app_config,
    total_gb=16,
    input_part_gb=0.125,
)

local_16gb_64par = dict(
    **local_base_app_config,
    total_gb=16,
    input_part_gb=0.25,
)

local_16gb_32par = dict(
    **local_base_app_config,
    total_gb=16,
    input_part_gb=0.5,
)

local_16gb_16par = dict(
    **local_base_app_config,
    total_gb=16,
    input_part_gb=1,
)

local_4gb_16par = dict(
    **local_base_app_config,
    total_gb=4,
    input_part_gb=0.25,
)

local_1gb_16par = dict(
    **local_base_app_config,
    total_gb=1,
    input_part_gb=0.0625,
)

configs = [
    # ------------------------------------------------------------
    #     Local experiments
    # ------------------------------------------------------------
    
    JobConfig(
        name="LocalNative",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_app_config),  # --> sort_two_stage()
    ),
    JobConfig(
        name="LocalNative64g64",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_64gb_64par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalNative32g64",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_32gb_64par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalNative32g32",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_32gb_32par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalNative32g16",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_32gb_16par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalNative16g128",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_16gb_128par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalNative16g64",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_16gb_64par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalNative16g32",
        cluster=local_cluster,
        system=dict(),
        app=dict(
            **local_16gb_32par,
            simple_shuffle=True,
            skip_output=True,
            ),
    ),
    JobConfig(
        name="LocalNative16g16",
        cluster=local_cluster,
        system=dict(),
        app=dict(
            **local_16gb_16par,
            simple_shuffle=True,
            skip_output=True,
            ),
    ),
    JobConfig(
        name="LocalNative4g16",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_4gb_16par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalNative1g16",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_1gb_16par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalSingle64g64",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_64gb_64par,
                 simple_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalSingle32g64",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_32gb_64par,
                 use_put=True,
                 naive_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalSingle32g32",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_32gb_32par,
                 naive_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalSingle32g16",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_32gb_16par,
                 naive_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalSingle16g128",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_16gb_128par,
                 naive_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalSingle16g64",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_16gb_64par,
                 naive_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalSingle16g32",
        cluster=local_cluster,
        system=dict(),
        app=dict(
            **local_16gb_32par,
            naive_shuffle=True,
            skip_output=True,
            ),
    ),
    JobConfig(
        name="LocalSingle16g16",
        cluster=local_cluster,
        system=dict(),
        app=dict(
            **local_16gb_16par,
            naive_shuffle=True,
            skip_output=True,
            ),
    ),
    JobConfig(
        name="LocalSingle4g16",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_4gb_16par,
                 naive_shuffle=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalSingle1g16",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_1gb_16par,
                 naive_shuffle=True,
                 skip_output=True,),
    ),    
    JobConfig(
        name="LocalReuse32g32",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_32gb_32par,
                 reuse=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalReuseSimple32g32",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_32gb_32par,
                 reuse_simple=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalReuse16g32",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_16gb_32par,
                 reuse=True,
                 skip_output=True,),
    ),
    JobConfig(
        name="LocalReuseSimple16g32",
        cluster=local_cluster,
        system=dict(),
        app=dict(**local_16gb_32par,
                 reuse_simple=True,
                 skip_output=True,),
    ),
]
