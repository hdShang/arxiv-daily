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

**提出ReVision视网膜基础模型，利用大规模远程医疗数据构建临床原生智能，以解决低资源环境下部署效率低的问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `视网膜基础模型` `临床原生智能` `远程医疗数据` `零样本学习` `部署效率` `图像-文本对齐` `低资源医疗AI` `眼科疾病检测`

## 📋 核心要点

1. 核心问题：现有视网膜基础模型依赖精选数据集，缺乏真实临床上下文，且需大量任务特定优化，导致低资源环境下部署效率低。
2. 方法要点：利用大规模远程医疗项目中的临床图像与报告自然对齐数据，构建ReVision模型，直接从真实医疗实践中学习临床原生智能。
3. 实验或效果：ReVision在零样本疾病检测中平均AUROC达0.946，辅助诊断准确性提升14.8%，并实现高效迁移到新任务和场景。

## 📝 摘要（中文）

当前视网膜基础模型受限于缺乏真实临床背景的精选研究数据集，且每个应用都需要大量任务特定优化，限制了其在低资源环境下的部署效率。本文表明，通过直接从真实世界医疗实践中构建临床原生智能，可以克服这些障碍。我们的核心见解是，大规模远程医疗项目（专家中心为分布式机构提供远程咨询）是学习临床图像解读的自然资源库。我们提出了ReVision，这是一个视网膜基础模型，它从485,980张彩色眼底照片及其对应诊断报告的自然对齐中学习，这些数据来自中国162家医疗机构长达十年的远程医疗项目积累。通过在27个眼科基准上进行广泛评估，我们证明ReVision能以最少的本地资源实现部署效率。无需任何任务特定训练，ReVision在12个公共基准上实现了平均AUROC为0.946的零样本疾病检测，在3个独立临床队列上为0.952。当最小适应可行时，ReVision匹配了经过广泛微调的替代方案，同时需要数量级更少的可训练参数和标记示例。学习到的表示还能有效迁移到新的临床站点、成像领域、成像模态和系统健康预测任务。在一项涉及33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助在所有经验水平上将诊断准确性提高了14.8%。这些结果表明，临床原生智能可以直接从临床档案中提取，无需进一步注释，以构建适合各种低资源环境的医疗AI系统。

## 🔬 方法详解

**问题定义**：论文旨在解决视网膜基础模型在低资源环境下部署效率低的问题。现有方法依赖精选研究数据集，缺乏真实临床上下文，且每个应用都需要大量任务特定优化，导致资源消耗大、适应性差。

**核心思路**：论文的核心思路是从大规模远程医疗实践中直接提取临床原生智能。远程医疗项目自然产生图像与诊断报告的对齐数据，这为学习临床图像解读提供了丰富、真实的资源，无需额外标注，从而克服数据稀缺和优化负担。

**技术框架**：整体架构基于从485,980张彩色眼底照片及其对应诊断报告中学习对齐表示。模型通过预训练阶段，利用图像-文本对进行自监督学习，捕获临床语义信息。然后，在评估阶段，模型支持零样本推理或最小适应，应用于多种眼科任务，如疾病检测和健康预测。

**关键创新**：最重要的技术创新是直接从真实世界临床档案中构建基础模型，无需人工标注。与现有方法依赖精选数据集和大量微调不同，ReVision利用远程医疗的自然对齐数据，实现了临床原生智能的提取，本质区别在于数据来源和优化效率的提升。

**关键设计**：关键设计包括使用大规模图像-文本对进行预训练，可能采用对比学习或生成式方法对齐视觉和语言特征。模型架构可能基于Transformer或卷积网络，具体参数设置未知，但强调最小化可训练参数和标记示例需求，以支持低资源部署。损失函数可能设计为最大化图像与报告之间的语义一致性，但具体细节未在摘要中说明。

## 📊 实验亮点

最重要的实验结果包括：零样本疾病检测在12个公共基准上平均AUROC达0.946，在3个独立临床队列上为0.952；最小适应时匹配微调模型，但参数和示例需求大幅减少；前瞻性读者研究中，零样本辅助将33名眼科医生的诊断准确性提升14.8%；模型表示能有效迁移到新临床站点、成像域和健康预测任务。

## 🎯 应用场景

该研究在低资源医疗环境中具有广泛潜在应用，如远程眼科诊断、基层医疗筛查和疾病监测。通过减少对标注数据和计算资源的需求，ReVision能提升医疗AI的普及性和效率，未来可能扩展到其他医学影像领域，推动个性化医疗和健康预测。

## 📄 摘要（原文）

> Current retinal foundation models remain constrained by curated research datasets that lack authentic clinical context, and require extensive task-specific optimization for each application, limiting their deployment efficiency in low-resource settings. Here, we show that these barriers can be overcome by building clinical native intelligence directly from real-world medical practice. Our key insight is that large-scale telemedicine programs, where expert centers provide remote consultations across distributed facilities, represent a natural reservoir for learning clinical image interpretation. We present ReVision, a retinal foundation model that learns from the natural alignment between 485,980 color fundus photographs and their corresponding diagnostic reports, accumulated through a decade-long telemedicine program spanning 162 medical institutions across China. Through extensive evaluation across 27 ophthalmic benchmarks, we demonstrate that ReVison enables deployment efficiency with minimal local resources. Without any task-specific training, ReVision achieves zero-shot disease detection with an average AUROC of 0.946 across 12 public benchmarks and 0.952 on 3 independent clinical cohorts. When minimal adaptation is feasible, ReVision matches extensively fine-tuned alternatives while requiring orders of magnitude fewer trainable parameters and labeled examples. The learned representations also transfer effectively to new clinical sites, imaging domains, imaging modalities, and systemic health prediction tasks. In a prospective reader study with 33 ophthalmologists, ReVision's zero-shot assistance improved diagnostic accuracy by 14.8% across all experience levels. These results demonstrate that clinical native intelligence can be directly extracted from clinical archives without any further annotation to build medical AI systems suited to various low-resource settings.

