---
layout: default
title: DORAEMON: A Unified Library for Visual Object Modeling and Representation Learning at Scale
---

# DORAEMON: A Unified Library for Visual Object Modeling and Representation Learning at Scale

**arXiv**: [2511.04394v1](https://arxiv.org/abs/2511.04394) | [PDF](https://arxiv.org/pdf/2511.04394.pdf)

**作者**: Ke Du, Yimin Peng, Chao Gao, Fan Zhou, Siqiao Xue

---

## 💡 一句话要点

**提出DORAEMON统一库以支持大规模视觉对象建模和表示学习**

**关键词**: `视觉对象建模` `表示学习` `PyTorch库` `YAML驱动工作流` `预训练骨干网络` `ONNX导出`

## 📋 核心要点

1. 核心问题：视觉对象建模和表示学习在不同尺度下缺乏统一工具
2. 方法要点：基于PyTorch，通过YAML配置集成分类、检索和度量学习
3. 实验或效果：在ImageNet-1K等数据集上复现或超越参考结果

## 📄 摘要（原文）

> DORAEMON is an open-source PyTorch library that unifies visual object
> modeling and representation learning across diverse scales. A single
> YAML-driven workflow covers classification, retrieval and metric learning; more
> than 1000 pretrained backbones are exposed through a timm-compatible interface,
> together with modular losses, augmentations and distributed-training utilities.
> Reproducible recipes match or exceed reference results on ImageNet-1K,
> MS-Celeb-1M and Stanford online products, while one-command export to ONNX or
> HuggingFace bridges research and deployment. By consolidating datasets, models,
> and training techniques into one platform, DORAEMON offers a scalable
> foundation for rapid experimentation in visual recognition and representation
> learning, enabling efficient transfer of research advances to real-world
> applications. The repository is available at https://github.com/wuji3/DORAEMON.

