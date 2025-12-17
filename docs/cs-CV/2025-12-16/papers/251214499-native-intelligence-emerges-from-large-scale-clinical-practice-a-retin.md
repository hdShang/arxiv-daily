---
layout: default
title: Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency
---

# Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14499" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14499</a>
  <a href="https://arxiv.org/pdf/2512.14499.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14499" onclick="toggleFavorite(this, '2512.14499', 'Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Guo, Jiawei Du, Shengzhu Yang, Shuai Lu, Wenquan Cheng, Kaiwen Zhang, Yihua Sun, Chuhong Yang, Weihang Zhang, Fang Chen, Yilan Wu, Lie Ju, Guochen Ning, Longfei Ma, Huiping Yao, Jinyuan Wang, Peilun Shi, Yukun Zhou, Jie Xu, Pearse A. Keane, Hanruo Liu, Hongen Liao, Ningli Wang, Huiqi Li

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**ReVision：基于大规模临床实践的视网膜原生智能模型，提升部署效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视网膜疾病诊断` `眼底图像分析` `远程医疗` `深度学习` `迁移学习`

## 📋 核心要点

1. 现有视网膜基础模型依赖人工标注数据集，缺乏真实临床环境，且任务特定优化需求高，限制了低资源环境下的部署。
2. ReVision利用大规模远程医疗数据中眼底照片与诊断报告的自然对齐关系，学习临床原生智能，无需额外标注。
3. 实验表明，ReVision在零样本疾病检测中表现出色，且能有效迁移到新场景，显著提升医生诊断准确率。

## 📝 摘要（中文）

现有的视网膜基础模型受限于缺乏真实临床背景的人工数据集，并且需要针对每个应用进行大量的任务特定优化，限制了其在低资源环境中的部署效率。本文提出ReVision，一个从真实医疗实践中学习临床原生智能的视网膜基础模型。核心思想是，大型远程医疗项目（专家中心为分布式机构提供远程咨询）是学习临床图像解读的天然资源。ReVision从中国162家医疗机构十年远程医疗项目中积累的485,980张彩色眼底照片及其诊断报告的自然对齐关系中学习。在27个眼科基准测试中，ReVision以最小的本地资源实现了部署效率。在没有任何任务特定训练的情况下，ReVision在12个公共基准测试中实现了0.946的平均AUROC，在3个独立的临床队列中实现了0.952的平均AUROC。当最小限度的适应可行时，ReVision匹配了经过大量微调的替代方案，同时需要的可训练参数和标记示例的数量级更少。学习到的表征也能有效地转移到新的临床站点、成像领域、成像模式和全身健康预测任务。在对33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助将所有经验水平的诊断准确率提高了14.8%。这些结果表明，可以直接从临床档案中提取临床原生智能，而无需任何进一步的注释，从而构建适用于各种低资源环境的医疗AI系统。

## 🔬 方法详解

**问题定义**：现有视网膜基础模型依赖于经过精心策划的研究数据集，这些数据集通常缺乏真实的临床背景，并且需要针对每个特定任务进行大量的优化。这限制了它们在资源有限的环境中的部署效率。因此，如何构建一个能够直接从真实临床数据中学习，并且具有良好泛化能力和部署效率的视网膜基础模型是一个关键问题。

**核心思路**：论文的核心思路是利用大规模远程医疗项目中积累的眼底照片和诊断报告之间的自然对齐关系，构建一个能够学习临床原生智能的视网膜基础模型。这种方法避免了对大量人工标注数据的依赖，并且能够更好地捕捉真实临床场景中的复杂性和多样性。

**技术框架**：ReVision的整体框架包括以下几个主要部分：1) 数据收集：收集来自大规模远程医疗项目的眼底照片和对应的诊断报告。2) 数据预处理：对图像进行标准化处理，并对诊断报告进行文本解析和结构化。3) 模型训练：使用对比学习或自监督学习等方法，训练一个能够将眼底照片映射到高质量表征空间的深度学习模型。4) 零样本推理：利用学习到的表征空间，进行零样本疾病检测和诊断。5) 微调适应：在少量标注数据上进行微调，以适应新的临床站点、成像领域或成像模式。

**关键创新**：ReVision的关键创新在于其利用了大规模远程医疗数据中固有的自然对齐关系，避免了对大量人工标注数据的依赖。这种方法使得模型能够直接从真实临床数据中学习，从而更好地捕捉临床场景中的复杂性和多样性。此外，ReVision还具有良好的泛化能力和部署效率，能够有效地迁移到新的临床站点、成像领域和成像模式。

**关键设计**：论文中没有明确给出关键的参数设置、损失函数、网络结构等技术细节。但是，可以推测，ReVision可能采用了以下一些关键设计：1) 使用Transformer或卷积神经网络作为基础架构，以提取图像特征。2) 使用对比学习或自监督学习等方法，训练模型学习高质量的表征空间。3) 使用合适的损失函数，例如InfoNCE损失或交叉熵损失，来优化模型。4) 使用数据增强技术，例如随机裁剪、旋转和颜色抖动，来提高模型的鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14499/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14499/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14499/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ReVision在27个眼科基准测试中表现出色，在没有任何任务特定训练的情况下，在12个公共基准测试中实现了0.946的平均AUROC，在3个独立的临床队列中实现了0.952的平均AUROC。在对33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助将所有经验水平的诊断准确率提高了14.8%。

## 🎯 应用场景

ReVision具有广泛的应用前景，可用于远程医疗、基层医疗机构的眼科疾病辅助诊断，提高诊断效率和准确性。该模型还可应用于眼科疾病的早期筛查、风险评估和个性化治疗方案制定。未来，ReVision有望与其他医疗影像模态和临床数据相结合，实现更全面的健康管理。

## 📄 摘要（原文）

> Current retinal foundation models remain constrained by curated research datasets that lack authentic clinical context, and require extensive task-specific optimization for each application, limiting their deployment efficiency in low-resource settings. Here, we show that these barriers can be overcome by building clinical native intelligence directly from real-world medical practice. Our key insight is that large-scale telemedicine programs, where expert centers provide remote consultations across distributed facilities, represent a natural reservoir for learning clinical image interpretation. We present ReVision, a retinal foundation model that learns from the natural alignment between 485,980 color fundus photographs and their corresponding diagnostic reports, accumulated through a decade-long telemedicine program spanning 162 medical institutions across China. Through extensive evaluation across 27 ophthalmic benchmarks, we demonstrate that ReVison enables deployment efficiency with minimal local resources. Without any task-specific training, ReVision achieves zero-shot disease detection with an average AUROC of 0.946 across 12 public benchmarks and 0.952 on 3 independent clinical cohorts. When minimal adaptation is feasible, ReVision matches extensively fine-tuned alternatives while requiring orders of magnitude fewer trainable parameters and labeled examples. The learned representations also transfer effectively to new clinical sites, imaging domains, imaging modalities, and systemic health prediction tasks. In a prospective reader study with 33 ophthalmologists, ReVision's zero-shot assistance improved diagnostic accuracy by 14.8% across all experience levels. These results demonstrate that clinical native intelligence can be directly extracted from clinical archives without any further annotation to build medical AI systems suited to various low-resource settings.

