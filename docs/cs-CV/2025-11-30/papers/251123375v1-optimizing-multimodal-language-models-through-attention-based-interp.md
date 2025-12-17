---
layout: default
title: Optimizing Multimodal Language Models through Attention-based Interpretability
---

# Optimizing Multimodal Language Models through Attention-based Interpretability

**arXiv**: [2511.23375v1](https://arxiv.org/abs/2511.23375) | [PDF](https://arxiv.org/pdf/2511.23375.pdf)

**作者**: Alexander Sergeev, Evgeny Kotelnikov

---

## 💡 一句话要点

**提出基于注意力的可解释性方法，以优化多模态语言模型的参数高效微调**

**关键词**: `多模态语言模型` `参数高效微调` `注意力机制` `可解释性` `图像理解` `图像描述生成`

## 📋 核心要点

1. 多模态语言模型难以解释，影响参数高效微调中关键组件的选择
2. 通过分析注意力分数识别关注图像关键对象的注意力头，并计算Head Impact分数量化其重要性
3. 实验表明微调高HI分数层能显著提升图像理解能力，仅需微调约0.01%参数

## 📄 摘要（原文）

> Modern large language models become multimodal, analyzing various data formats like text and images. While fine-tuning is effective for adapting these multimodal language models (MLMs) to downstream tasks, full fine-tuning is computationally expensive. Parameter-Efficient Fine-Tuning (PEFT) methods address this by training only a small portion of model weights. However, MLMs are difficult to interpret, making it challenging to identify which components are most effective for training to balance efficiency and performance. We propose an attention-based interpretability method for MLMs by analyzing attention scores relative to image tokens. The core idea is to identify attention heads that focus on image key objects. We utilize this information to select optimal model components for PEFT in multimodal models. Our contributions include a method for identifying attention heads associated with image key objects, its application to PEFT for image captioning, and the creation of a new dataset containing images, key object masks, and their textual descriptions. We conducted experiments on MLMs with 2-3 billion parameters to validate the method's effectiveness. By calculating Head Impact (HI) scores we quantify an attention head's focus on key objects, indicating its significance in image understanding. Our fine-tuning experiments demonstrate that adapting layers with the highest HI scores leads to the most significant shifts in metrics compared to pre-trained, randomly selected, or lowest-HI-score layers. This indicates that fine-tuning a small percentage (around 0.01%) of parameters in these crucial layers can substantially influence image understanding capabilities.

