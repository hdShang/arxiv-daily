---
layout: default
title: Video2Layout: Recall and Reconstruct Metric-Grounded Cognitive Map for Spatial Reasoning
---

# Video2Layout: Recall and Reconstruct Metric-Grounded Cognitive Map for Spatial Reasoning

**arXiv**: [2511.16160v1](https://arxiv.org/abs/2511.16160) | [PDF](https://arxiv.org/pdf/2511.16160.pdf)

**作者**: Yibin Huang, Wang Xu, Wanyue Zhang, Helu Zhi, Jingjing Huang, Yangbin Xu, Yangang Sun, Conghui Zhu, Tiejun Zhao

---

## 💡 一句话要点

**提出Video2Layout框架，通过连续边界坐标重建空间布局以解决细粒度空间推理问题**

**关键词**: `空间推理` `认知地图` `视频理解` `连续坐标` `强化微调` `基准评估`

## 📋 核心要点

1. 核心问题：现有网格认知地图方法依赖离散栅格表示，限制细粒度空间推理能力
2. 方法要点：使用连续对象边界坐标量化物理距离和大小，结合监督和强化微调阶段
3. 实验或效果：在QVS-Bench等基准上，V2LO-7B模型平均提升4.92%，验证方法优越性

## 📄 摘要（原文）

> Spatial intelligence is a critical frontier for Multimodal Large Language Models (MLLMs), empowering them to comprehend the physical world. Drawing inspiration from human perception mechanisms, existing studies attempt to construct a coherent spatial understanding via grid-based cognitive maps from multi-frame visual inputs. However, current grid-based map methods rely on discretized raster representations, which limit the model's ability in fine-grained spatial reasoning. To overcome this limitation, we propose Video2Layout, a framework for reconstructing metric-grounded spatial layouts from video. The framework employs continuous object boundary coordinates to quantify inter-object physical distances and object size. This empowers the model with quantitative spatial computation capabilities, effectively alleviating the inherent ambiguity when describing spatial relationships in natural language. Specifically, our method comprises two core stages. First, in supervised fine-tuning stage, we construct a high-quality dataset from the AI2THOR simulator, which enables the model to learn the mapping from visual inputs to precise boundary coordinates. Subsequently, a reinforcement fine-tuning stage further enhances the model's real-world generalization capabilities. To systematically evaluate the correlation between cognitive map accuracy and image quantity, as well as how the quantity of image inputs affects spatial reasoning accuracy, we introduce QVS-Bench, a diagnostic benchmark designed to analyze the relevant mechanisms. Evaluated on QVS-Bench and mainstream spatial reasoning benchmarks, our model, V2LO-7B achieves an average improvement of 4.92% over the model trained on grid maps, validating the superiority of our method. Our code is available at https://github.com/ybrrraway/Video2Layout.

