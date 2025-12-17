---
layout: default
title: Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency
---

# Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency

**arXiv**: [2512.14499v1](https://arxiv.org/abs/2512.14499) | [PDF](https://arxiv.org/pdf/2512.14499.pdf)

**作者**: Jia Guo, Jiawei Du, Shengzhu Yang, Shuai Lu, Wenquan Cheng, Kaiwen Zhang, Yihua Sun, Chuhong Yang, Weihang Zhang, Fang Chen, Yilan Wu, Lie Ju, Guochen Ning, Longfei Ma, Huiping Yao, Jinyuan Wang, Peilun Shi, Yukun Zhou, Jie Xu, Pearse A. Keane, Hanruo Liu, Hongen Liao, Ningli Wang, Huiqi Li

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出ReVision视网膜基础模型，从大规模临床实践中学习，以解决低资源环境下部署效率低的问题。**

**关键词**: `视网膜基础模型` `临床原生智能` `远程医疗数据` `零样本学习` `部署效率` `多模态对齐` `低资源医疗AI` `眼科图像分析`

## 📋 核心要点

1. 核心问题：现有视网膜基础模型依赖精选数据集，缺乏真实临床上下文，且需大量任务特定优化，导致低资源环境下部署效率低。
2. 方法要点：从大规模远程医疗项目中学习临床图像与诊断报告的自然对齐，构建临床原生智能，无需额外标注。
3. 实验或效果：零样本疾病检测AUROC达0.946-0.952，最小适应下匹配微调模型，参数和样本需求大幅减少。

## 📝 摘要（中文）

当前视网膜基础模型受限于缺乏真实临床背景的精选研究数据集，且每个应用都需要大量任务特定优化，限制了其在低资源环境下的部署效率。本文表明，通过直接从真实世界医疗实践中构建临床原生智能，可以克服这些障碍。我们的核心见解是，大规模远程医疗项目（专家中心为分布式机构提供远程咨询）是学习临床图像解读的自然资源库。我们提出了ReVision，一个视网膜基础模型，它从485,980张彩色眼底照片及其对应诊断报告的自然对齐中学习，这些数据来自中国162家医疗机构长达十年的远程医疗项目积累。通过在27个眼科基准上进行广泛评估，我们证明ReVision能以最少的本地资源实现部署效率。无需任何任务特定训练，ReVision在12个公共基准上实现零样本疾病检测，平均AUROC为0.946，在3个独立临床队列上为0.952。当最小适应可行时，ReVision匹配经过广泛微调的替代方案，同时需要数量级更少的可训练参数和标记示例。学习到的表示还能有效迁移到新临床站点、成像领域、成像模态和系统健康预测任务。在一项涉及33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助将诊断准确性提高了14.8%，覆盖所有经验水平。这些结果表明，临床原生智能可以直接从临床档案中提取，无需进一步注释，以构建适合各种低资源环境的医疗AI系统。

## 🔬 方法详解

ReVision是一个视网膜基础模型，其整体框架基于大规模远程医疗数据构建，核心是从485,980张彩色眼底照片及其对应诊断报告的自然对齐中学习临床图像解读。关键技术创新点在于直接从真实世界临床实践中提取原生智能，利用远程医疗项目积累的数据，实现图像与文本的跨模态对齐学习。与现有方法的主要区别在于：现有方法通常依赖标注良好的研究数据集，而ReVision直接从临床档案中学习，无需额外人工标注；现有方法需要针对每个任务进行大量优化，而ReVision通过零样本或最小适应实现高效部署，减少了参数和样本需求。

## 📊 实验亮点

零样本疾病检测在12个公共基准上平均AUROC达0.946，在3个临床队列上达0.952；最小适应下匹配微调模型，参数和样本需求减少数量级；前瞻性读者研究中，零样本辅助将诊断准确性提高14.8%。

## 🎯 应用场景

该研究在低资源医疗环境中具有广泛应用价值，如远程眼科诊断、基层医疗机构辅助筛查、多模态医学图像分析，以及系统健康预测任务，能提升诊断效率和准确性，降低医疗成本。

## 📄 摘要（原文）

> Current retinal foundation models remain constrained by curated research datasets that lack authentic clinical context, and require extensive task-specific optimization for each application, limiting their deployment efficiency in low-resource settings. Here, we show that these barriers can be overcome by building clinical native intelligence directly from real-world medical practice. Our key insight is that large-scale telemedicine programs, where expert centers provide remote consultations across distributed facilities, represent a natural reservoir for learning clinical image interpretation. We present ReVision, a retinal foundation model that learns from the natural alignment between 485,980 color fundus photographs and their corresponding diagnostic reports, accumulated through a decade-long telemedicine program spanning 162 medical institutions across China. Through extensive evaluation across 27 ophthalmic benchmarks, we demonstrate that ReVison enables deployment efficiency with minimal local resources. Without any task-specific training, ReVision achieves zero-shot disease detection with an average AUROC of 0.946 across 12 public benchmarks and 0.952 on 3 independent clinical cohorts. When minimal adaptation is feasible, ReVision matches extensively fine-tuned alternatives while requiring orders of magnitude fewer trainable parameters and labeled examples. The learned representations also transfer effectively to new clinical sites, imaging domains, imaging modalities, and systemic health prediction tasks. In a prospective reader study with 33 ophthalmologists, ReVision's zero-shot assistance improved diagnostic accuracy by 14.8% across all experience levels. These results demonstrate that clinical native intelligence can be directly extracted from clinical archives without any further annotation to build medical AI systems suited to various low-resource settings.

