---
layout: default
title: Q-Save: Towards Scoring and Attribution for Generated Video Evaluation
---

# Q-Save: Towards Scoring and Attribution for Generated Video Evaluation

**arXiv**: [2511.18825v1](https://arxiv.org/abs/2511.18825) | [PDF](https://arxiv.org/pdf/2511.18825.pdf)

**作者**: Xiele Wu, Zicheng Zhang, Mingtao Chen, Yixian Liu, Yiming Liu, Shushi Wang, Zhichao Hu, Yuhong Liu, Guangtao Zhai, Xiaohong Liu

---

## 💡 一句话要点

**提出Q-Save基准数据集与模型，用于AI生成视频的全面可解释评估。**

**关键词**: `AI生成视频评估` `多维度标注` `SlowFast框架` `可解释AI` `质量评分与归因`

## 📋 核心要点

1. 核心问题：AI生成视频缺乏全面且可解释的质量评估基准。
2. 方法要点：构建多维度标注数据集，并基于SlowFast框架联合评分与归因。
3. 实验或效果：模型在视频质量预测上达到SOTA，并提供人类对齐的解释。

## 📄 摘要（原文）

> We present Q-Save, a new benchmark dataset and model for holistic and explainable evaluation of AI-generated video (AIGV) quality. The dataset contains near 10000 videos, each annotated with a scalar mean opinion score (MOS) and fine-grained attribution labels along three core dimensions: visual quality, dynamic quality, and text-video alignment. These multi-aspect annotations enable both accurate quality assessment and interpretable reasoning behind the scores. To leverage this data, we propose a unified evaluation model that jointly performs quality scoring and attribution-based explanation. The model adopts the SlowFast framework to distinguish between fast frames and slow frames - slow frames are processed with high resolution while fast frames use low resolution, balancing evaluation accuracy and computational efficiency. For training, we use data formatted in Chain-of-Thought (COT) style and employ a multi-stage strategy: we first conduct Supervised Fine-Tuning (SFT), then further enhance the model with Grouped Relative Policy Optimization (GRPO), and finally perform SFT again to improve model stability. Experimental results demonstrate that our model achieves state-of-the-art performance in video quality prediction while also providing human-aligned, interpretable justifications. Our dataset and model establish a strong foundation for explainable evaluation in generative video research, contributing to the development of multimodal generation and trustworthy AI. Code and dataset will be released upon publication.

