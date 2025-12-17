---
layout: default
title: Two-Stage Vision Transformer for Image Restoration: Colorization Pretraining + Residual Upsampling
---

# Two-Stage Vision Transformer for Image Restoration: Colorization Pretraining + Residual Upsampling

**arXiv**: [2512.02512v1](https://arxiv.org/abs/2512.02512) | [PDF](https://arxiv.org/pdf/2512.02512.pdf)

**作者**: Aditya Chaudhary, Prachet Dev Singh, Ankit Jha

---

## 💡 一句话要点

**提出ViT-SR，通过着色预训练和残差上采样两阶段策略提升单图像超分辨率性能。**

**关键词**: `单图像超分辨率` `视觉Transformer` `自监督预训练` `残差学习` `图像恢复`

## 📋 核心要点

1. 核心问题：单图像超分辨率（SISR）在计算机视觉中仍具挑战性。
2. 方法要点：采用两阶段训练，先自监督着色预训练学习通用视觉表示，再微调进行4倍超分辨率。
3. 实验或效果：在DIV2K数据集上实现SSIM 0.712和PSNR 22.90 dB，验证方法有效性。

## 📄 摘要（原文）

> In computer vision, Single Image Super-Resolution (SISR) is still a difficult problem. We present ViT-SR, a new technique to improve the performance of a Vision Transformer (ViT) employing a two-stage training strategy. In our method, the model learns rich, generalizable visual representations from the data itself through a self-supervised pretraining phase on a colourization task. The pre-trained model is then adjusted for 4x super-resolution. By predicting the addition of a high-frequency residual image to an initial bicubic interpolation, this design simplifies residual learning. ViT-SR, trained and evaluated on the DIV2K benchmark dataset, achieves an impressive SSIM of 0.712 and PSNR of 22.90 dB. These results demonstrate the efficacy of our two-stage approach and highlight the potential of self-supervised pre-training for complex image restoration tasks. Further improvements may be possible with larger ViT architectures or alternative pretext tasks.

