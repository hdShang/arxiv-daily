---
layout: default
title: HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control
---

# HydroGEM: A Self Supervised Zero Shot Hybrid TCN Transformer Foundation Model for Continental Scale Streamflow Quality Control

**arXiv**: [2512.14106v1](https://arxiv.org/abs/2512.14106) | [PDF](https://arxiv.org/pdf/2512.14106.pdf)

**作者**: Ijaz Ul Haq, Byung Suk Lee, Julia N. Perdrial, David Baude

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Supplementary materials, datasets, and implementation code will be made publicly available upon acceptance for publication in a peer-reviewed journal

---

## 💡 一句话要点

**提出HydroGEM自监督零样本混合TCN-Transformer基础模型，用于大陆尺度河流流量质量控制，以解决远程传感器数据质量维护的挑战。**

**关键词**: `水文监测` `自监督学习` `零样本迁移` `混合TCN-Transformer` `异常检测` `基础模型` `数据质量控制` `时间序列分析`

## 📋 核心要点

1. 现有方法依赖人工维护河流流量数据质量，效率低且难以扩展到大陆尺度远程传感器网络。
2. 提出HydroGEM基础模型，通过自监督预训练和混合TCN-Transformer架构学习水文表示，实现异常检测与重建。
3. 在合成测试中，检测F1达0.792，重建误差降低68.7%，零样本跨国迁移F1=0.586，显著优于基线方法。

## 📝 摘要（中文）

实时河流流量监测网络每年产生数百万观测数据，但维护数千个远程传感器的数据质量仍依赖人工。本文介绍HydroGEM（水文通用监测编码器），这是一个用于大陆尺度河流流量质量控制的基础模型。HydroGEM采用两阶段训练：首先在来自3,724个美国地质调查局站点的603万序列上进行自监督预训练，学习水文表示；然后使用合成异常进行微调，用于检测和重建。模型采用混合TCN-Transformer架构（1420万参数），捕捉局部时间模式和长程依赖，同时通过分层归一化处理六个数量级的流量变化。在包含799个站点和18种专家验证异常类型的保留合成测试中，HydroGEM在检测上达到F1=0.792，重建误差降低68.7%，比现有方法提升36.3%。零样本迁移到100个加拿大环境与气候变化部站点，F1=0.586，超越所有基线，展示了跨国泛化能力。模型在不同校正幅度下保持一致的检测性能，并与操作季节性模式对齐。HydroGEM设计用于人机协同工作流——输出为需要专家审核的质量控制建议，而非自主校正。

## 🔬 方法详解

HydroGEM采用两阶段训练框架：首先，自监督预训练从大量水文序列中学习通用表示；其次，微调阶段使用合成异常优化检测和重建任务。核心创新包括混合TCN-Transformer架构，结合时间卷积网络（TCN）捕捉局部时间模式和Transformer处理长程依赖，以及分层归一化技术应对流量数据的广泛动态范围。与现有方法相比，HydroGEM通过基础模型设计实现零样本泛化，减少对标注数据的依赖，并整合多尺度时间特征，提升异常检测的准确性和鲁棒性。

## 📊 实验亮点

HydroGEM在合成测试中检测F1达0.792，重建误差降低68.7%，比现有方法提升36.3%；零样本跨国迁移到加拿大站点，F1=0.586，展示强泛化能力，且检测性能在不同校正幅度和季节性模式下保持稳定。

## 🎯 应用场景

该研究可应用于全球河流流量监测网络的数据质量控制，支持环境监测、水资源管理和气候研究，通过自动化建议减轻专家负担，提高数据可靠性。

## 📄 摘要（原文）

> Real-time streamflow monitoring networks generate millions of observations annually, yet maintaining data quality across thousands of remote sensors remains labor-intensive. We introduce HydroGEM (Hydrological Generalizable Encoder for Monitoring), a foundation model for continental-scale streamflow quality control. HydroGEM uses two-stage training: self-supervised pretraining on 6.03 million sequences from 3,724 USGS stations learns hydrological representations, followed by fine-tuning with synthetic anomalies for detection and reconstruction. A hybrid TCN-Transformer architecture (14.2M parameters) captures local temporal patterns and long-range dependencies, while hierarchical normalization handles six orders of magnitude in discharge. On held-out synthetic tests comprising 799 stations with 18 expert-validated anomaly types, HydroGEM achieves F1 = 0.792 for detection and 68.7% reconstruction-error reduction, a 36.3% improvement over existing methods. Zero-shot transfer to 100 Environment and Climate Change Canada stations yields F1 = 0.586, exceeding all baselines and demonstrating cross-national generalization. The model maintains consistent detection across correction magnitudes and aligns with operational seasonal patterns. HydroGEM is designed for human-in-the-loop workflows - outputs are quality control suggestions requiring expert review, not autonomous corrections.

