from sacred import Experiment


ex = Experiment("FIBER")


@ex.config
def config():
    seed = 0
    datasets = ["vqa"]
    val_mode = "min"

    # Image settings
    train_transform_keys = ["albef"]
    val_transform_keys = ["albef"]
    image_size = 576
    vit = "swin_base_patch4_window12_384_in22k"
    image_only = False
    draw_false_image = 0
    input_image_embed_size = 1024
    resolution_before = 384
    pretrained_vit = False

    # Text settings
    vqav2_label_size = 3129
    max_text_len = 50
    tokenizer = "roberta-base"
    vocab_size = 50265
    whole_word_masking = False
    mlm_prob = 0.15
    draw_false_text = 0
    input_text_embed_size = 768

    # Transformer settings
    hidden_size = 768
    num_heads = 12
    num_layers = 12
    mlp_ratio = 4
    drop_rate = 0.1
    num_fuse_block = 6
    itc_pooler = True

    # Optimizer settings
    learning_rate = 5e-5
    max_epoch = 100
    batch_size = 1

    # PL Trainer settings
    resume_from = None
    test_only = False

    # below params varies with the environment
    data_root = ""
    log_dir = "result"
    per_gpu_batchsize = 1
    num_gpus = 4
    num_nodes = 1
    load_path = ""
    num_workers = 20
    precision = 32

    # VQA settings
    is_cp = False

    # VAE settings
    hidden_dims = [512, 512]
    latent_size = 512
    n_components = 128
    n_samples = 128