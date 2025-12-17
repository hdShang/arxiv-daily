---
layout: default
title: Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency
---

# Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14499" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14499v1</a>
  <a href="https://arxiv.org/pdf/2512.14499.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14499v1" onclick="toggleFavorite(this, '2512.14499v1', 'Native Intelligence Emerges from Large-Scale Clinical Practice: A Retinal Foundation Model with Deployment Efficiency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jia Guo, Jiawei Du, Shengzhu Yang, Shuai Lu, Wenquan Cheng, Kaiwen Zhang, Yihua Sun, Chuhong Yang, Weihang Zhang, Fang Chen, Yilan Wu, Lie Ju, Guochen Ning, Longfei Ma, Huiping Yao, Jinyuan Wang, Peilun Shi, Yukun Zhou, Jie Xu, Pearse A. Keane, Hanruo Liu, Hongen Liao, Ningli Wang, Huiqi Li

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**ReVision：基于大规模临床实践的视网膜原生智能模型，提升部署效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视网膜基础模型` `临床原生智能` `远程医疗` `零样本学习` `眼科疾病诊断`

## 📋 核心要点

1. 现有视网膜基础模型依赖人工标注数据集，缺乏真实临床环境，且针对不同任务需大量优化，部署效率低。
2. ReVision利用大规模远程医疗项目积累的眼底照片和诊断报告，学习临床图像解读，构建临床原生智能。
3. ReVision在多个眼科任务上表现出色，无需或仅需少量微调即可达到甚至超越现有模型，显著提升部署效率。

## 📝 摘要（中文）

现有的视网膜基础模型受限于缺乏真实临床背景的人工数据集，并且需要针对每个应用进行大量的任务特定优化，限制了其在低资源环境中的部署效率。本文提出ReVision，一个从真实医疗实践中学习临床原生智能的视网膜基础模型。核心思想是，大规模远程医疗项目是学习临床图像解读的天然资源库。ReVision从中国162家医疗机构十年远程医疗项目中积累的485,980张彩色眼底照片及其诊断报告的自然对齐关系中学习。在27个眼科基准测试中，ReVision在极少本地资源下实现了高效部署。无需任何任务特定训练，ReVision在12个公共基准测试中实现了0.946的平均AUROC，在3个独立临床队列中实现了0.952的平均AUROC。在少量适配的情况下，ReVision匹配了经过大量微调的替代方案，同时所需的可训练参数和标记示例减少了几个数量级。学习到的表征有效地迁移到新的临床站点、成像领域、成像模式和全身健康预测任务。在对33名眼科医生的前瞻性读者研究中，ReVision的零样本辅助将诊断准确率提高了14.8%。这些结果表明，可以直接从临床档案中提取临床原生智能，而无需任何进一步的注释，从而构建适用于各种低资源环境的医疗AI系统。

## 🔬 方法详解

**问题定义**：现有视网膜基础模型依赖于人工标注的、规模有限的数据集，这些数据集往往不能充分代表真实的临床场景。此外，这些模型通常需要针对不同的下游任务进行大量的任务特定优化和微调，这不仅耗费计算资源，也限制了它们在资源匮乏环境中的部署和应用。因此，如何构建一个能够直接从真实临床数据中学习，并且具有良好泛化能力和部署效率的视网膜基础模型是一个亟待解决的问题。

**核心思路**：本文的核心思路是利用大规模远程医疗项目中积累的眼底照片和诊断报告之间的自然对齐关系，将远程医疗项目视为一个天然的临床图像解读学习资源库。通过在这种大规模、真实世界的临床数据上进行预训练，模型可以学习到更加鲁棒和泛化的视网膜图像表征，从而在各种下游任务中实现更好的性能和更高的部署效率。

**技术框架**：ReVision的整体框架包括以下几个主要阶段：1) 数据收集：从中国162家医疗机构的远程医疗项目中收集了485,980张彩色眼底照片及其对应的诊断报告。2) 模型预训练：使用收集到的数据对模型进行预训练，学习眼底图像的通用表征。3) 零样本评估：在多个公开的眼科基准数据集上进行零样本评估，验证模型的泛化能力。4) 微调评估：在少量标注数据上进行微调，评估模型在不同任务上的性能。5) 临床医生评估：与33名眼科医生合作进行前瞻性研究，评估ReVision在实际临床应用中的效果。

**关键创新**：ReVision的关键创新在于：1) 利用大规模远程医疗数据构建临床原生智能，避免了对人工标注数据的依赖。2) 提出了一个高效的预训练策略，使得模型能够学习到具有良好泛化能力的视网膜图像表征。3) 通过零样本和少量微调的实验，证明了ReVision在各种眼科任务上的优越性能和部署效率。与现有方法相比，ReVision能够直接从真实临床数据中学习，无需大量的任务特定优化，从而降低了部署成本和难度。

**关键设计**：论文中没有详细描述具体的网络结构和损失函数等技术细节，但可以推测其可能采用了Transformer或卷积神经网络等常用的图像处理模型，并结合对比学习或掩码图像建模等预训练技术，以学习到具有良好判别性和泛化能力的图像表征。此外，论文强调了利用大规模临床数据的自然对齐关系进行学习，这可能涉及到一些数据处理和对齐的技术细节，但具体实现方式未知。

## 📊 实验亮点

ReVision在27个眼科基准测试中表现出色，无需任何任务特定训练，在12个公共基准测试中实现了0.946的平均AUROC，在3个独立临床队列中实现了0.952的平均AUROC。在少量适配的情况下，ReVision匹配了经过大量微调的替代方案，同时所需的可训练参数和标记示例减少了几个数量级。在与33名眼科医生的前瞻性研究中，ReVision的零样本辅助将诊断准确率提高了14.8%。

## 🎯 应用场景

ReVision具有广泛的应用前景，可用于眼科疾病的早期筛查、诊断辅助、远程医疗等领域。尤其是在医疗资源匮乏的地区，ReVision可以帮助医生提高诊断准确率和效率，从而改善患者的治疗效果。未来，ReVision还可以扩展到其他医学影像领域，为构建更加智能化的医疗AI系统奠定基础。

## 📄 摘要（原文）

> Current retinal foundation models remain constrained by curated research datasets that lack authentic clinical context, and require extensive task-specific optimization for each application, limiting their deployment efficiency in low-resource settings. Here, we show that these barriers can be overcome by building clinical native intelligence directly from real-world medical practice. Our key insight is that large-scale telemedicine programs, where expert centers provide remote consultations across distributed facilities, represent a natural reservoir for learning clinical image interpretation. We present ReVision, a retinal foundation model that learns from the natural alignment between 485,980 color fundus photographs and their corresponding diagnostic reports, accumulated through a decade-long telemedicine program spanning 162 medical institutions across China. Through extensive evaluation across 27 ophthalmic benchmarks, we demonstrate that ReVison enables deployment efficiency with minimal local resources. Without any task-specific training, ReVision achieves zero-shot disease detection with an average AUROC of 0.946 across 12 public benchmarks and 0.952 on 3 independent clinical cohorts. When minimal adaptation is feasible, ReVision matches extensively fine-tuned alternatives while requiring orders of magnitude fewer trainable parameters and labeled examples. The learned representations also transfer effectively to new clinical sites, imaging domains, imaging modalities, and systemic health prediction tasks. In a prospective reader study with 33 ophthalmologists, ReVision's zero-shot assistance improved diagnostic accuracy by 14.8% across all experience levels. These results demonstrate that clinical native intelligence can be directly extracted from clinical archives without any further annotation to build medical AI systems suited to various low-resource settings.

