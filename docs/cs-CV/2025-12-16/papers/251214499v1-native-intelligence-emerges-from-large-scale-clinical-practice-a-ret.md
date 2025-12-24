---
layout: default
title: "Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency"
---

# Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14499" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14499v1</a>
  <a href="https://arxiv.org/pdf/2512.14499.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14499v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14499v1', 'Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Guo, Jiawei Du, Shengzhu Yang, Shuai Lu, Wenquan Cheng, Kaiwen Zhang, Yihua Sun, Chuhong Yang, Weihang Zhang, Fang Chen, Yilan Wu, Lie Ju, Guochen Ning, Longfei Ma, Huiping Yao, Jinyuan Wang, Peilun Shi, Yukun Zhou, Jie Xu, Pearse A. Keane, Hanruo Liu, Hongen Liao, Ningli Wang, Huiqi Li

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**ReVision：基于大规模临床实践的视网膜原生智能模型，提升部署效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视网膜疾病诊断` `眼底图像分析` `远程医疗` `深度学习` `迁移学习`

## 📋 核心要点

1. 现有视网膜基础模型依赖人工标注数据集，缺乏真实临床环境数据，且需大量任务特定优化，限制了低资源环境部署。
2. ReVision利用大规模远程医疗项目积累的眼底照片和诊断报告，学习临床图像解读，构建临床原生智能。
3. ReVision在多个眼科基准测试中表现出色，零样本疾病检测AUROC高达0.946，并能有效迁移到新场景。

## 📝 摘要（中文）

现有的视网膜基础模型受限于缺乏真实临床背景的人工数据集，并且需要针对每个应用进行大量的任务特定优化，限制了其在低资源环境中的部署效率。本文提出ReVision，一个从真实医疗实践中学习临床原生智能的视网膜基础模型。核心思想是，大规模远程医疗项目是学习临床图像解读的天然资源库。ReVision从中国162家医疗机构十年远程医疗项目中积累的485,980张彩色眼底照片及其诊断报告的自然对齐中学习。在27个眼科基准测试中，ReVision在极少本地资源的情况下实现了高效部署。无需任何任务特定训练，ReVision在12个公共基准测试中实现了0.946的平均AUROC，在3个独立临床队列中实现了0.952的平均AUROC。当进行少量适配时，ReVision在需要少几个数量级的可训练参数和标记样本的情况下，匹配了经过大量微调的替代方案。学习到的表征有效地迁移到新的临床站点、成像领域、成像方式和全身健康预测任务。在对33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助将诊断准确率提高了14.8%。这些结果表明，可以直接从临床档案中提取临床原生智能，而无需任何进一步的注释，从而构建适用于各种低资源环境的医疗AI系统。

## 🔬 方法详解

**问题定义**：现有视网膜基础模型依赖于经过精心策划的研究数据集，这些数据集通常缺乏真实的临床环境信息。此外，这些模型通常需要针对特定任务进行大量的优化和微调，这使得它们在资源有限的环境中难以部署和应用。因此，如何构建一个能够从真实临床数据中学习，并且具有良好泛化能力和部署效率的视网膜基础模型是一个关键问题。

**核心思路**：本文的核心思路是利用大规模远程医疗项目产生的海量眼底图像和诊断报告作为训练数据，从中学习临床原生智能。远程医疗项目天然地提供了图像和诊断报告之间的对齐关系，这使得模型能够直接从真实临床实践中学习，而无需额外的人工标注。这种方法能够更好地捕捉临床数据的复杂性和多样性，从而提高模型的泛化能力和鲁棒性。

**技术框架**：ReVision的整体框架包括数据收集、模型训练和评估三个主要阶段。首先，从大规模远程医疗项目中收集眼底图像和对应的诊断报告。然后，利用这些数据训练一个深度学习模型，该模型能够学习图像和诊断报告之间的映射关系。最后，在多个眼科基准测试中评估模型的性能，包括零样本疾病检测、少量样本微调和跨领域迁移学习。

**关键创新**：ReVision的关键创新在于它直接从真实临床实践中学习临床原生智能，而无需依赖人工标注的数据集。这种方法能够更好地捕捉临床数据的复杂性和多样性，从而提高模型的泛化能力和鲁棒性。此外，ReVision还能够实现高效的部署，因为它只需要少量的计算资源和数据即可进行微调。

**关键设计**：ReVision使用了Transformer架构作为其核心模型，并采用对比学习方法来训练模型。具体来说，模型的目标是学习将眼底图像和对应的诊断报告映射到同一个嵌入空间中，使得相似的图像和报告在嵌入空间中距离更近，而不相似的图像和报告距离更远。此外，作者还设计了一种新的损失函数，该损失函数能够更好地平衡不同疾病之间的样本数量差异。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14499v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14499v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14499v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ReVision在27个眼科基准测试中表现出色。在零样本疾病检测中，ReVision在12个公共基准测试中实现了0.946的平均AUROC，在3个独立临床队列中实现了0.952的平均AUROC。在少量样本微调中，ReVision在需要少几个数量级的可训练参数和标记样本的情况下，匹配了经过大量微调的替代方案。此外，ReVision的零样本辅助将眼科医生的诊断准确率提高了14.8%。

## 🎯 应用场景

ReVision具有广泛的应用前景，可用于眼科疾病的辅助诊断、远程医疗、疾病筛查和健康管理。尤其是在低资源地区，ReVision能够帮助医生提高诊断准确率和效率，从而改善患者的医疗服务质量。未来，ReVision还可以扩展到其他医学影像领域，例如X光、CT和MRI等，为构建智能医疗系统提供强大的技术支持。

## 📄 摘要（原文）

> Current retinal foundation models remain constrained by curated research datasets that lack authentic clinical context, and require extensive task-specific optimization for each application, limiting their deployment efficiency in low-resource settings. Here, we show that these barriers can be overcome by building clinical native intelligence directly from real-world medical practice. Our key insight is that large-scale telemedicine programs, where expert centers provide remote consultations across distributed facilities, represent a natural reservoir for learning clinical image interpretation. We present ReVision, a retinal foundation model that learns from the natural alignment between 485,980 color fundus photographs and their corresponding diagnostic reports, accumulated through a decade-long telemedicine program spanning 162 medical institutions across China. Through extensive evaluation across 27 ophthalmic benchmarks, we demonstrate that ReVison enables deployment efficiency with minimal local resources. Without any task-specific training, ReVision achieves zero-shot disease detection with an average AUROC of 0.946 across 12 public benchmarks and 0.952 on 3 independent clinical cohorts. When minimal adaptation is feasible, ReVision matches extensively fine-tuned alternatives while requiring orders of magnitude fewer trainable parameters and labeled examples. The learned representations also transfer effectively to new clinical sites, imaging domains, imaging modalities, and systemic health prediction tasks. In a prospective reader study with 33 ophthalmologists, ReVision's zero-shot assistance improved diagnostic accuracy by 14.8% across all experience levels. These results demonstrate that clinical native intelligence can be directly extracted from clinical archives without any further annotation to build medical AI systems suited to various low-resource settings.

