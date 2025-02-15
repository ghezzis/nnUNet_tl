from batchgenerators.utilities.file_and_folder_operations import *
import numpy as np
from nnunet.paths import preprocessing_output_dir

#remove comment only if you do it
#otherwise it is done everytime you call the nnunet

tasks = [
     #"Task803__peaks__PYT_L__TractoInferno",
    # "Task709__peaks__ILF_L__TractoInferno",
    # "Task704__T1__IFOF_L__TractoInferno",
    # "Task705__AP__IFOF_L__TractoInferno",
    #Task706__peaks__IFOF_L__TractoInferno",
    # "Task807__T1__PT_L__fold_0__Apss__TractoDim",
    # "Task808__T1__PT_L__fold_1__Apss__TractoDim",
    # "Task809__T1__PT_L__fold_2__Apss__TractoDim",
    # "Task810__T1__PT_L__fold_3__Apss__TractoDim",
    # "Task811__T1__PT_L__fold_4__Apss__TractoDim",
    # "Task812__AP__PT_L__fold_0__Apss__TractoDim",
    # "Task813__AP__PT_L__fold_1__Apss__TractoDim",
    # "Task814__AP__PT_L__fold_2__Apss__TractoDim",
    # "Task815__AP__PT_L__fold_3__Apss__TractoDim",
    # "Task816__AP__PT_L__fold_4__Apss__TractoDim",
    #     "Task817__peaks__PT_L__fold_0__Apss__TractoDim",
    # "Task818__peaks__PT_L__fold_1__Apss__TractoDim",
    # "Task819__peaks__PT_L__fold_2__Apss__TractoDim",
    # "Task820__peaks__PT_L__fold_3__Apss__TractoDim",
    # "Task821__peaks__PT_L__fold_4__Apss__TractoDim",

    # "Task822__T1__AF_L__fold_0__Apss__TractoDim",
    # "Task823__T1__AF_L__fold_1__Apss__TractoDim",
    # "Task824__T1__AF_L__fold_2__Apss__TractoDim",
    # "Task825__T1__AF_L__fold_3__Apss__TractoDim",
    # "Task826__T1__AF_L__fold_4__Apss__TractoDim",
    #     "Task827__AP__AF_L__fold_0__Apss__TractoDim",
    # "Task828__AP__AF_L__fold_1__Apss__TractoDim",
    # "Task829__AP__AF_L__fold_2__Apss__TractoDim",
    # "Task830__AP__AF_L__fold_3__Apss__TractoDim",
    # "Task831__AP__AF_L__fold_4__Apss__TractoDim",
    #     "Task832__peaks__AF_L__fold_0__Apss__TractoDim",
    # "Task833__peaks__AF_L__fold_1__Apss__TractoDim",
    # "Task834__peaks__AF_L__fold_2__Apss__TractoDim",
    # "Task835__peaks__AF_L__fold_3__Apss__TractoDim",
    # "Task836__peaks__AF_L__fold_4__Apss__TractoDim",
]

for task_name in tasks:
    # make sure to run the Task601 dataset conversion and
    # nnUNet_plan_and_preprocess first!
    plans_fname = join(preprocessing_output_dir, task_name, 'nnUNetPlansv2.1_plans_3D.pkl')
    plans = load_pickle(plans_fname)
    plans['plans_per_stage'][0]['batch_size'] = 2
    #plans['plans_per_stage'][0]['num_pool_per_axis'] = [7, 7]
    # because we changed the num_pool_per_axis, we need to change conv_kernel_sizes and pool_op_kernel_sizes as well!
    #plans['plans_per_stage'][0]['pool_op_kernel_sizes'] = [[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2]]
    #plans['plans_per_stage'][0]['conv_kernel_sizes'] = [[3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3]]
    # for a network with num_pool_per_axis [7,7] the correct length of pool kernel sizes is 7 and the length of conv
    # kernel sizes is 8! Note that you can also change these numbers if you believe it makes sense. A pool kernel size
    # of 1 will result in no pooling along that axis, a kernel size of 3 will reduce the size of the feature map
    # representations by factor 3 instead of 2.

    # save the plans under a new plans name. Note that the new plans file must end with _plans_2D.pkl!
    save_pickle(plans, join(preprocessing_output_dir, task_name, 'nnUNetPlansv2.1_plans_3D.pkl'))

# %%
