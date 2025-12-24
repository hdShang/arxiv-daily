---
layout: default
title: "CKD-EHR:Clinical Knowledge Distillation for Electronic Health Records"
---

# CKD-EHR:Clinical Knowledge Distillation for Electronic Health Records

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15118" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15118v1</a>
  <a href="https://arxiv.org/pdf/2506.15118.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15118v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15118v1', 'CKD-EHR:Clinical Knowledge Distillation for Electronic Health Records')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junke Wang, Hongshun Ling, Li Zhang, Longqian Zhang, Fang Wang, Yuan Gao, Zhi Li

**分类**: cs.CL

**发布日期**: 2025-06-18

**备注**: 20 pages,5 figures

**🔗 代码/项目**: [GITHUB](https://github.com/209506702/CKD_EHR)

---

## 💡 一句话要点

**提出CKD-EHR框架以解决电子健康记录中的疾病预测效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电子健康记录` `疾病预测` `知识蒸馏` `临床决策支持` `模型优化` `医学知识表示` `轻量级模型`

## 📋 核心要点

1. 现有的EHR疾病预测模型在医学知识表示和临床部署效率上存在不足，限制了其应用效果。
2. CKD-EHR框架通过知识蒸馏技术，利用大型语言模型生成可解释的软标签，并将其转移到轻量级模型中。
3. 在MIMIC-III数据集上，CKD-EHR的诊断准确率提高了9%，F1-score提升了27%，推理速度提升了22.2倍。

## 📝 摘要（中文）

基于电子健康记录（EHR）的疾病预测模型在促进精准医疗和早期干预方面具有显著临床价值。然而，现有的大型语言模型面临两个主要挑战：医学知识表示不足和临床部署效率低。为了解决这些问题，本研究提出了CKD-EHR（临床知识蒸馏框架），通过知识蒸馏技术实现高效且准确的疾病风险预测。具体而言，首先对大型语言模型Qwen2.5-7B进行医学知识增强数据的微调，使其作为教师模型。然后，通过多粒度注意力蒸馏机制生成可解释的软标签。最后，将蒸馏的知识转移到轻量级BERT学生模型上。实验结果表明，在MIMIC-III数据集上，CKD-EHR显著优于基线模型：诊断准确率提高9%，F1-score提升27%，推理速度提升22.2倍。这一创新解决方案不仅大幅提高了资源利用效率，还显著增强了诊断的准确性和及时性，为临床环境中的资源优化提供了实用的技术途径。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有EHR疾病预测模型在医学知识表示不足和临床部署效率低下的问题。这些问题导致模型在实际应用中的效果不佳。

**核心思路**：CKD-EHR框架的核心思路是通过知识蒸馏技术，将大型语言模型的医学知识有效转移到轻量级模型中，以提高预测的准确性和效率。这样的设计旨在克服现有模型的局限性，实现更高效的临床应用。

**技术框架**：CKD-EHR的整体架构包括三个主要模块：首先，使用医学知识增强数据对大型语言模型Qwen2.5-7B进行微调；其次，通过多粒度注意力蒸馏机制生成可解释的软标签；最后，将蒸馏的知识转移到轻量级BERT学生模型中。

**关键创新**：CKD-EHR的主要创新在于引入了多粒度注意力蒸馏机制，使得生成的软标签更具解释性，并有效提升了轻量级模型的性能。这一方法与传统的知识蒸馏技术相比，能够更好地捕捉医学知识的复杂性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化蒸馏过程，同时在网络结构上对BERT模型进行了轻量化处理，以确保在保持性能的同时提高推理速度。

## 📊 实验亮点

在MIMIC-III数据集上的实验结果显示，CKD-EHR框架的诊断准确率提高了9%，F1-score提升了27%，推理速度实现了22.2倍的提升。这些显著的性能改进表明该框架在实际应用中的有效性和优势。

## 🎯 应用场景

CKD-EHR框架在医疗领域具有广泛的应用潜力，特别是在疾病预测和早期干预方面。通过提高模型的准确性和效率，该研究为临床决策支持系统提供了技术基础，能够帮助医生更快地做出诊断并优化资源配置，进而提升患者的治疗效果和满意度。

## 📄 摘要（原文）

> Electronic Health Records (EHR)-based disease prediction models have demonstrated significant clinical value in promoting precision medicine and enabling early intervention. However, existing large language models face two major challenges: insufficient representation of medical knowledge and low efficiency in clinical deployment. To address these challenges, this study proposes the CKD-EHR (Clinical Knowledge Distillation for EHR) framework, which achieves efficient and accurate disease risk prediction through knowledge distillation techniques. Specifically, the large language model Qwen2.5-7B is first fine-tuned on medical knowledge-enhanced data to serve as the teacher model.It then generates interpretable soft labels through a multi-granularity attention distillation mechanism. Finally, the distilled knowledge is transferred to a lightweight BERT student model. Experimental results show that on the MIMIC-III dataset, CKD-EHR significantly outperforms the baseline model:diagnostic accuracy is increased by 9%, F1-score is improved by 27%, and a 22.2 times inference speedup is achieved. This innovative solution not only greatly improves resource utilization efficiency but also significantly enhances the accuracy and timeliness of diagnosis, providing a practical technical approach for resource optimization in clinical settings. The code and data for this research are available athttps://github.com/209506702/CKD_EHR.

