---
layout: default
title: Animal Re-Identification on Microcontrollers
---

# Animal Re-Identification on Microcontrollers

**arXiv**: [2512.08198v1](https://arxiv.org/abs/2512.08198) | [PDF](https://arxiv.org/pdf/2512.08198.pdf)

**作者**: Yubo Chen, Di Zhao, Yun Sing Koh, Talia Xu

---

## 💡 一句话要点

**提出基于微控制器的动物重识别框架，实现低功耗边缘设备上的高效部署**

**关键词**: `动物重识别` `微控制器部署` `低分辨率输入` `知识蒸馏` `边缘计算` `数据高效微调`

## 📋 核心要点

1. 核心问题：现有动物重识别模型在微控制器上因内存小和输入分辨率低而难以部署
2. 方法要点：通过缩放MobileNetV2骨干网络，设计适应低分辨率输入的高精度架构
3. 实验或效果：在六个公共数据集上，模型尺寸减少两个数量级，保持竞争性检索准确率

## 📄 摘要（原文）

> Camera-based animal re-identification (Animal Re-ID) can support wildlife monitoring and precision livestock management in large outdoor environments with limited wireless connectivity. In these settings, inference must run directly on collar tags or low-power edge nodes built around microcontrollers (MCUs), yet most Animal Re-ID models are designed for workstations or servers and are too large for devices with small memory and low-resolution inputs. We propose an on-device framework. First, we characterise the gap between state-of-the-art Animal Re-ID models and MCU-class hardware, showing that straightforward knowledge distillation from large teachers offers limited benefit once memory and input resolution are constrained. Second, guided by this analysis, we design a high-accuracy Animal Re-ID architecture by systematically scaling a CNN-based MobileNetV2 backbone for low-resolution inputs. Third, we evaluate the framework with a real-world dataset and introduce a data-efficient fine-tuning strategy to enable fast adaptation with just three images per animal identity at a new site. Across six public Animal Re-ID datasets, our compact model achieves competitive retrieval accuracy while reducing model size by over two orders of magnitude. On a self-collected cattle dataset, the deployed model performs fully on-device inference with only a small accuracy drop and unchanged Top-1 accuracy relative to its cluster version. We demonstrate that practical, adaptable Animal Re-ID is achievable on MCU-class devices, paving the way for scalable deployment in real field environments.

