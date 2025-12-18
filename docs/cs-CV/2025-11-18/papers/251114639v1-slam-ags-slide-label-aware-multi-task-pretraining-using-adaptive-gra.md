---
layout: default
title: SLAM-AGS: Slide-Label Aware Multi-Task Pretraining Using Adaptive Gradient Surgery in Computational Cytology
---

# SLAM-AGS: Slide-Label Aware Multi-Task Pretraining Using Adaptive Gradient Surgery in Computational Cytology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14639" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14639v1</a>
  <a href="https://arxiv.org/pdf/2511.14639.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14639v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14639v1', 'SLAM-AGS: Slide-Label Aware Multi-Task Pretraining Using Adaptive Gradient Surgery in Computational Cytology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marco Acerbis, Swarnadip Chatterjee, Christophe Avenel, Joakim Lindblad

**分类**: cs.CV

**发布日期**: 2025-11-18

**备注**: 5 pages, 2 figures, Submitted to ISBI2026

**🔗 代码/项目**: [GITHUB](https://github.com/Ace95/SLAM-AGS)

---

## 💡 一句话要点

**SLAM-AGS：计算细胞学中基于自适应梯度手术的Slide-Label感知多任务预训练**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `计算细胞学` `多任务学习` `弱监督学习` `自监督学习` `梯度手术` `多示例学习` `骨髓细胞学`

## 📋 核心要点

1. 计算细胞学中，实例标签获取成本高昂且质量差，阳性样本比例极低，限制了模型训练效果。
2. SLAM-AGS框架通过联合优化弱监督相似性和自监督对比目标，并使用自适应梯度手术稳定训练过程。
3. 实验表明，在低阳性样本比例下，SLAM-AGS在包级别F1分数和阳性细胞检索方面显著优于其他预训练方法。

## 📝 摘要（中文）

计算细胞学面临两大挑战：i) 实例级别的标签不可靠且获取成本高昂，ii) 阳性样本比例极低。我们提出了SLAM-AGS，一个Slide-Label感知的多任务预训练框架，它联合优化(i) slide-negative patches上的弱监督相似性目标和(ii) slide-positive patches上的自监督对比目标，从而在下游任务中获得更强的性能。为了稳定学习，我们应用自适应梯度手术来解决冲突的任务梯度并防止模型崩溃。我们将预训练的编码器集成到基于注意力的多示例学习聚合器中，用于包级别的预测和对包中最异常实例的注意引导检索。在一个公开的骨髓细胞学数据集上，模拟阳性样本比例从10%降至0.5%，SLAM-AGS在包级别F1分数和Top 400阳性细胞检索方面优于其他预训练方法，尤其是在低阳性样本比例下增益最大，表明解决梯度干扰能够实现稳定的预训练并在下游任务中获得更好的性能。为了方便重现，我们以开源形式分享了完整的实现和评估框架：https://github.com/Ace95/SLAM-AGS。

## 🔬 方法详解

**问题定义**：计算细胞学中，细胞图像的实例级别标注成本高昂且质量难以保证，同时阳性细胞的比例通常极低，这给模型的训练带来了极大的挑战。现有的方法难以有效利用有限的标注信息，并且容易受到类别不平衡的影响，导致模型性能不佳。

**核心思路**：SLAM-AGS的核心思路是利用slide-level的弱标签信息，通过多任务学习的方式，同时学习slide-negative patches的相似性和slide-positive patches的对比特征。通过这种方式，模型可以更好地利用有限的标注信息，并且能够学习到更鲁棒的特征表示。此外，为了解决多任务学习中梯度冲突的问题，引入了自适应梯度手术，从而稳定训练过程。

**技术框架**：SLAM-AGS的整体框架包括三个主要部分：预训练阶段、多示例学习聚合阶段和检索阶段。在预训练阶段，使用slide-level的弱标签信息，通过多任务学习的方式，同时学习slide-negative patches的相似性和slide-positive patches的对比特征。在多示例学习聚合阶段，将预训练的编码器集成到基于注意力的多示例学习聚合器中，用于包级别的预测。在检索阶段，利用注意力机制引导检索包中最异常的实例。

**关键创新**：SLAM-AGS的关键创新在于以下几个方面：1) 提出了Slide-Label感知的多任务预训练框架，能够有效利用slide-level的弱标签信息。2) 引入了自适应梯度手术，解决了多任务学习中梯度冲突的问题，从而稳定训练过程。3) 将预训练的编码器集成到基于注意力的多示例学习聚合器中，用于包级别的预测和异常实例检索。

**关键设计**：在多任务学习中，使用了弱监督相似性损失和自监督对比损失。弱监督相似性损失用于学习slide-negative patches的相似性，自监督对比损失用于学习slide-positive patches的对比特征。自适应梯度手术通过动态调整每个任务的梯度方向，从而解决梯度冲突的问题。注意力机制用于学习每个实例的重要性，从而实现包级别的预测和异常实例检索。

## 📊 实验亮点

在骨髓细胞学数据集上，SLAM-AGS在低阳性样本比例（0.5%-10%）下，显著提升了包级别F1分数和Top 400阳性细胞检索性能，超越了其他预训练方法。例如，在0.5%阳性样本比例下，F1分数提升超过5%，表明该方法在数据稀缺场景下的有效性。

## 🎯 应用场景

SLAM-AGS在计算细胞学领域具有广泛的应用前景，可用于辅助诊断血液肿瘤、感染性疾病等。该方法能够有效利用有限的标注信息，提高诊断效率和准确性，降低诊断成本。未来，该方法有望推广到其他医学图像分析领域，例如病理图像分析、放射影像分析等。

## 📄 摘要（原文）

> Computational cytology faces two major challenges: i) instance-level labels are unreliable and prohibitively costly to obtain, ii) witness rates are extremely low. We propose SLAM-AGS, a Slide-Label-Aware Multitask pretraining framework that jointly optimizes (i) a weakly supervised similarity objective on slide-negative patches and (ii) a self-supervised contrastive objective on slide-positive patches, yielding stronger performance on downstream tasks. To stabilize learning, we apply Adaptive Gradient Surgery to tackle conflicting task gradients and prevent model collapse. We integrate the pretrained encoder into an attention-based Multiple Instance Learning aggregator for bag-level prediction and attention-guided retrieval of the most abnormal instances in a bag. On a publicly available bone-marrow cytology dataset, with simulated witness rates from 10% down to 0.5%, SLAM-AGS improves bag-level F1-Score and Top 400 positive cell retrieval over other pretraining methods, with the largest gains at low witness rates, showing that resolving gradient interference enables stable pretraining and better performance on downstream tasks. To facilitate reproducibility, we share our complete implementation and evaluation framework as open source: https://github.com/Ace95/SLAM-AGS.

