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

**提出ReVision视网膜基础模型，从大规模临床实践中提取原生智能，以解决低资源环境下部署效率问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `视网膜基础模型` `临床原生智能` `远程医疗` `零样本学习` `多模态对齐` `部署效率` `眼科AI` `弱监督学习`

## 📋 核心要点

1. 现有视网膜基础模型依赖精选数据集，缺乏真实临床背景，且需大量任务特定优化，部署效率低。
2. 从大规模远程医疗项目中学习临床图像与报告的自然对齐，构建临床原生智能基础模型。
3. 零样本疾病检测AUROC达0.946-0.952，最小适应下匹配微调模型，辅助诊断提升14.8%。

## 📝 摘要（中文）

当前视网膜基础模型受限于缺乏真实临床背景的精选研究数据集，且每个应用都需要大量任务特定优化，限制了其在低资源环境下的部署效率。本文表明，通过直接从真实世界医疗实践中构建临床原生智能可以克服这些障碍。我们的核心见解是，大规模远程医疗项目（专家中心为分布式机构提供远程咨询）是学习临床图像解读的自然资源库。我们提出了ReVision，这是一个视网膜基础模型，它从485,980张彩色眼底照片及其对应诊断报告的自然对齐中学习，这些数据来自中国162家医疗机构长达十年的远程医疗项目积累。通过对27个眼科基准的广泛评估，我们证明ReVision能以最少的本地资源实现部署效率。在没有任何任务特定训练的情况下，ReVision在12个公共基准上实现了平均AUROC为0.946的零样本疾病检测，在3个独立临床队列上为0.952。当最小适应可行时，ReVision匹配了经过广泛微调的替代方案，同时需要数量级更少的可训练参数和标记示例。学习到的表示还能有效迁移到新的临床站点、成像域、成像模态和全身健康预测任务。在一项涉及33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助在所有经验水平上将诊断准确性提高了14.8%。这些结果表明，临床原生智能可以直接从临床档案中提取，无需进一步注释，以构建适合各种低资源环境的医疗AI系统。

## 🔬 方法详解

**问题定义**：论文旨在解决视网膜基础模型在低资源环境下部署效率低的问题。现有方法依赖精选研究数据集，缺乏真实临床多样性，且每个应用需大量任务特定优化，导致资源消耗大、适应性差。

**核心思路**：核心思路是从大规模临床实践中直接提取“临床原生智能”，利用远程医疗项目中自然积累的图像-报告对齐数据，构建无需额外标注的基础模型，实现高效部署。

**技术框架**：整体框架基于大规模预训练。首先，从十年远程医疗项目中收集485,980张彩色眼底照片及对应诊断报告，覆盖162家机构。然后，通过自监督或弱监督学习对齐图像与文本报告，学习通用表示。最后，在27个眼科基准上评估零样本或最小适应性能。

**关键创新**：最重要的创新是“临床原生智能”概念，直接从真实临床工作流中学习，而非人工标注数据集。本质区别在于利用自然对齐数据，减少对标注的依赖，提升模型在真实场景中的泛化能力和部署效率。

**关键设计**：关键设计包括使用大规模异构临床数据（485,980样本），可能采用视觉-语言对齐技术（如图像-报告匹配），损失函数可能基于对比学习或跨模态预测。网络结构可能基于Transformer或CNN，具体细节未知，但强调最小化可训练参数（如仅微调少量层）以实现高效适应。

## 📊 实验亮点

零样本疾病检测在12个公共基准上平均AUROC达0.946，在3个临床队列上达0.952。最小适应下匹配微调模型，可训练参数和标记示例减少数量级。前瞻性读者研究中，零样本辅助将33名眼科医生的诊断准确性提升14.8%。模型能有效迁移到新站点、成像域和全身健康任务。

## 🎯 应用场景

该研究在低资源医疗环境中具有广泛应用潜力，如远程眼科筛查、基层医疗诊断辅助和疾病监测。实际价值在于减少对专家标注和计算资源的依赖，提升AI系统在真实临床场景中的可及性和效率。未来可能推动医疗AI向更普惠、自适应方向发展，支持多模态健康预测。

## 📄 摘要（原文）

> Current retinal foundation models remain constrained by curated research datasets that lack authentic clinical context, and require extensive task-specific optimization for each application, limiting their deployment efficiency in low-resource settings. Here, we show that these barriers can be overcome by building clinical native intelligence directly from real-world medical practice. Our key insight is that large-scale telemedicine programs, where expert centers provide remote consultations across distributed facilities, represent a natural reservoir for learning clinical image interpretation. We present ReVision, a retinal foundation model that learns from the natural alignment between 485,980 color fundus photographs and their corresponding diagnostic reports, accumulated through a decade-long telemedicine program spanning 162 medical institutions across China. Through extensive evaluation across 27 ophthalmic benchmarks, we demonstrate that ReVison enables deployment efficiency with minimal local resources. Without any task-specific training, ReVision achieves zero-shot disease detection with an average AUROC of 0.946 across 12 public benchmarks and 0.952 on 3 independent clinical cohorts. When minimal adaptation is feasible, ReVision matches extensively fine-tuned alternatives while requiring orders of magnitude fewer trainable parameters and labeled examples. The learned representations also transfer effectively to new clinical sites, imaging domains, imaging modalities, and systemic health prediction tasks. In a prospective reader study with 33 ophthalmologists, ReVision's zero-shot assistance improved diagnostic accuracy by 14.8% across all experience levels. These results demonstrate that clinical native intelligence can be directly extracted from clinical archives without any further annotation to build medical AI systems suited to various low-resource settings.

