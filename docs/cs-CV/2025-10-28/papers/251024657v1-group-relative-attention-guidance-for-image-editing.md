---
layout: default
title: Group Relative Attention Guidance for Image Editing
---

# Group Relative Attention Guidance for Image Editing

**arXiv**: [2510.24657v1](https://arxiv.org/abs/2510.24657) | [PDF](https://arxiv.org/pdf/2510.24657.pdf)

**作者**: Xuanpu Zhang, Xuesong Niu, Ruidong Chen, Dan Song, Jianhao Zeng, Penghui Du, Haoxiang Cao, Kai Wu, An-an Liu

---

## 💡 一句话要点

**提出Group Relative Attention Guidance以增强图像编辑的连续精细控制**

**关键词**: `图像编辑` `扩散变换器模型` `注意力机制` `编辑强度控制` `无调优方法`

## 📋 核心要点

1. 现有图像编辑方法缺乏对编辑程度的有效控制，限制定制化结果
2. 基于DiT模型的MM-Attention机制，重加权token delta值以调节编辑强度
3. 实验显示GRAG可无缝集成，提升编辑质量，实现比Classifier-Free Guidance更平滑精确的控制

## 📄 摘要（原文）

> Recently, image editing based on Diffusion-in-Transformer models has
> undergone rapid development. However, existing editing methods often lack
> effective control over the degree of editing, limiting their ability to achieve
> more customized results. To address this limitation, we investigate the
> MM-Attention mechanism within the DiT model and observe that the Query and Key
> tokens share a bias vector that is only layer-dependent. We interpret this bias
> as representing the model's inherent editing behavior, while the delta between
> each token and its corresponding bias encodes the content-specific editing
> signals. Based on this insight, we propose Group Relative Attention Guidance, a
> simple yet effective method that reweights the delta values of different tokens
> to modulate the focus of the model on the input image relative to the editing
> instruction, enabling continuous and fine-grained control over editing
> intensity without any tuning. Extensive experiments conducted on existing image
> editing frameworks demonstrate that GRAG can be integrated with as few as four
> lines of code, consistently enhancing editing quality. Moreover, compared to
> the commonly used Classifier-Free Guidance, GRAG achieves smoother and more
> precise control over the degree of editing. Our code will be released at
> https://github.com/little-misfit/GRAG-Image-Editing.

