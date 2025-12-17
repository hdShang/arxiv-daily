---
layout: default
title: Glaucoma Detection and Structured OCT Report Generation via a Fine-tuned Multimodal Large Language Model
---

# Glaucoma Detection and Structured OCT Report Generation via a Fine-tuned Multimodal Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02403" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02403v1</a>
  <a href="https://arxiv.org/pdf/2510.02403.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02403v1" onclick="toggleFavorite(this, '2510.02403v1', 'Glaucoma Detection and Structured OCT Report Generation via a Fine-tuned Multimodal Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jalil Jalili, Yashraj Gavhane, Evan Walker, Anna Heinke, Christopher Bowd, Akram Belghith, Massimo A. Fazio, Christopher A. Girkin, C. Gustavo De Moraes, Jeffrey M. Liebmann, Sally L. Baxter, Robert N. Weinreb, Linda M. Zangwill, Mark Christopher

**分类**: q-bio.QM, cs.AI, cs.CV

**发布日期**: 2025-10-01

---

## 💡 一句话要点

**微调多模态大语言模型用于青光眼检测和结构化OCT报告生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `青光眼检测` `多模态大语言模型` `OCT图像分析` `视网膜神经纤维层` `临床报告生成`

## 📋 核心要点

1. 现有青光眼诊断依赖人工阅片，耗时且易受主观因素影响，缺乏自动化和可解释性。
2. 本文提出一种基于微调Llama 3.2 Vision-Instruct模型的多模态大语言模型，用于自动生成结构化OCT报告。
3. 实验结果表明，该模型在青光眼检测和RNFL变薄评估方面表现出高准确率，并能有效识别图像质量问题。

## 📝 摘要（中文）

本研究旨在开发一种可解释的多模态大语言模型(MM-LLM)，用于(1)筛查视神经乳头(ONH)OCT环扫图像的质量，以及(2)生成结构化的临床报告，包括青光眼诊断和分区域的视网膜神经纤维层(RNFL)变薄评估。研究采用回顾性队列设计，使用了来自DIGS和ADAGES队列的1310名受试者的43849张Spectralis ONH OCT环扫图像（1331只青光眼眼和867只健康眼）。通过微调MM-LLM（Llama 3.2 Vision-Instruct模型）来生成OCT成像数据的临床描述。训练数据包括配对的OCT图像和自动生成的结构化临床报告，描述了全局和分区域的RNFL变薄情况。低质量扫描被标记为不可用，并与固定的拒绝声明配对。该模型在保留的测试集上进行了三个任务的评估：质量评估、青光眼检测和七个解剖区域的RNFL变薄分类。评估指标包括准确率、灵敏度、特异性、精确率和F1分数。还使用标准文本评估指标评估了模型描述的质量。结果表明，该模型在质量评估中达到了0.90的准确率和0.98的特异性。对于青光眼检测，准确率为0.86（灵敏度0.91，特异性0.73，F1分数为0.91）。RNFL变薄预测的准确率范围为0.83至0.94，在全局和颞侧区域表现最佳。文本生成分数显示与参考报告高度一致（BLEU：0.82；ROUGE-1：0.94；ROUGE-2：0.87；ROUGE-L：0.92；BERTScore-F1：0.99）。结论是，微调后的MM-LLM能够基于OCT成像生成准确的临床描述，并在识别图像质量问题和检测青光眼方面表现出高准确率。该模型还提供了RNFL变薄的分区域描述，以帮助支持临床OCT评估。

## 🔬 方法详解

**问题定义**：该论文旨在解决青光眼诊断中人工阅片效率低、主观性强的问题。现有方法在自动化生成结构化临床报告方面存在不足，难以提供可解释的诊断依据，并且对OCT图像质量的评估不够准确。

**核心思路**：论文的核心思路是利用多模态大语言模型(MM-LLM)同时处理OCT图像和文本信息，通过微调Llama 3.2 Vision-Instruct模型，使其能够理解OCT图像的特征，并生成包含青光眼诊断和RNFL变薄评估的结构化临床报告。这种方法结合了图像处理和自然语言处理的优势，提高了诊断的准确性和可解释性。

**技术框架**：整体框架包括数据预处理、模型微调和评估三个主要阶段。首先，对OCT图像进行质量评估，并将低质量图像标记为不可用。然后，使用配对的OCT图像和自动生成的结构化临床报告对Llama 3.2 Vision-Instruct模型进行微调。最后，在保留的测试集上评估模型的质量评估、青光眼检测和RNFL变薄分类性能。

**关键创新**：该论文的关键创新在于将多模态大语言模型应用于青光眼诊断，并实现了自动生成结构化临床报告的功能。与传统的图像处理方法相比，该方法能够更好地理解OCT图像的上下文信息，并提供更全面的诊断依据。此外，该模型还能够评估OCT图像的质量，从而提高诊断的可靠性。

**关键设计**：该研究使用了Llama 3.2 Vision-Instruct模型作为基础模型，并对其进行了微调。训练数据包括配对的OCT图像和自动生成的结构化临床报告，其中包含了全局和分区域的RNFL变薄情况。损失函数未知，网络结构细节未知，但使用了标准文本评估指标（BLEU、ROUGE、BERTScore）来评估生成报告的质量。

## 📊 实验亮点

该模型在质量评估中达到了0.90的准确率和0.98的特异性。对于青光眼检测，准确率为0.86（灵敏度0.91，特异性0.73，F1分数为0.91）。RNFL变薄预测的准确率范围为0.83至0.94，在全局和颞侧区域表现最佳。文本生成分数显示与参考报告高度一致（BLEU：0.82；ROUGE-1：0.94；ROUGE-2：0.87；ROUGE-L：0.92；BERTScore-F1：0.99）。

## 🎯 应用场景

该研究成果可应用于眼科临床辅助诊断，提高青光眼筛查效率和准确性，减少人工阅片的工作量。通过自动生成结构化报告，有助于医生更好地理解病情，制定个性化的治疗方案。未来，该技术有望推广到其他眼科疾病的诊断和管理中。

## 📄 摘要（原文）

> Objective: To develop an explainable multimodal large language model (MM-LLM) that (1) screens optic nerve head (ONH) OCT circle scans for quality and (2) generates structured clinical reports that include glaucoma diagnosis and sector-wise retinal nerve fiber layer (RNFL) thinning assessments. Design: Retrospective cohort study of 1,310 subjects contributing 43,849 Spectralis ONH OCT circle scans (1,331 glaucomatous and 867 healthy eyes) from the DIGS and ADAGES cohorts. Methods: A MM-LLM (Llama 3.2 Vision-Instruct model) was fine-tuned to generate clinical descriptions of OCT imaging data. Training data included paired OCT images and automatically generated, structured clinical reports that described global and sectoral RNFL thinning. Poor-quality scans were labeled as unusable and paired with a fixed refusal statement. The model was evaluated on a held-out test set for three tasks: quality assessment, glaucoma detection, and RNFL thinning classification across seven anatomical sectors. Evaluation metrics included accuracy, sensitivity, specificity, precision, and F1-score. Model description quality was also evaluated using standard text evaluation metrics. Results: The model achieved 0.90 accuracy and 0.98 specificity for quality triage. For glaucoma detection, accuracy was 0.86 (sensitivity 0.91, specificity 0.73, F1-score 0.91). RNFL thinning prediction accuracy ranged from 0.83 to 0.94, with highest performance in global and temporal sectors. Text generation scores showed strong alignment with reference reports (BLEU: 0.82; ROUGE-1: 0.94; ROUGE-2: 0.87; ROUGE-L: 0.92; BERTScore-F1: 0.99). Conclusions: The fine-tuned MM-LLM generated accurate clinical descriptions based on OCT imaging. The model achieved high accuracy in identifying image quality issues and detecting glaucoma. The model also provided sectoral descriptions of RNFL thinning to help support clinical OCT evaluation.

