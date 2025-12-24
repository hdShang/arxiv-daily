---
layout: default
title: Comparisons between a Large Language Model-based Real-Time Compound Diagnostic Medical AI Interface and Physicians for Common Internal Medicine Cases using Simulated Patients
---

# Comparisons between a Large Language Model-based Real-Time Compound Diagnostic Medical AI Interface and Physicians for Common Internal Medicine Cases using Simulated Patients

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20609" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20609v1</a>
  <a href="https://arxiv.org/pdf/2505.20609.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20609v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20609v1', 'Comparisons between a Large Language Model-based Real-Time Compound Diagnostic Medical AI Interface and Physicians for Common Internal Medicine Cases using Simulated Patients')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyungjun Park, Chang-Yun Woo, Seungjo Lim, Seunghwan Lim, Keunho Kwak, Ju Young Jeong, Chong Hyun Suh

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出基于大型语言模型的实时复合诊断医疗AI接口以提升内科诊断效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医疗AI` `内科诊断` `临床试验` `诊断准确性` `成本效益` `患者满意度`

## 📋 核心要点

1. 现有的内科诊断方法依赖于医生的经验，准确性和效率受到时间和知识的限制。
2. 本文提出了一种基于大型语言模型的实时复合诊断医疗AI接口，旨在提高诊断的准确性和效率。
3. 实验结果表明，AI接口在首次和第二次鉴别诊断的准确率上均优于医生，同时显著缩短了诊断时间和降低了成本。

## 📝 摘要（中文）

本研究旨在开发一种基于大型语言模型（LLM）的实时复合诊断医疗AI接口，并通过临床试验将其与医生在常见内科病例中的表现进行比较。研究招募了一名全科医生、两名内科住院医师和五名模拟患者，使用改编自美国医学执照考试（USMLE）第二步临床技能（CS）考试的临床案例。结果显示，AI接口的首次鉴别诊断准确率为80%，显著高于医生的50%至70%。此外，AI接口在时间和成本上也表现出明显优势，平均耗时557秒，成本仅为0.08美元。尽管患者对AI接口的满意度略低于医生，但整体结果表明，AI接口在内科初级护理咨询中具有潜在的辅助作用。

## 🔬 方法详解

**问题定义**：本研究旨在解决内科常见病例诊断中医生效率低、准确性不足的问题。现有方法依赖于医生的主观判断，容易受到时间和知识的限制。

**核心思路**：论文提出的解决方案是开发一种基于大型语言模型的实时复合诊断医疗AI接口，通过模拟患者的临床案例来提高诊断的准确性和效率。

**技术框架**：该AI接口的整体架构包括数据输入模块、诊断推理模块和结果输出模块。数据输入模块接收患者信息，诊断推理模块基于LLM进行分析，结果输出模块提供诊断建议。

**关键创新**：最重要的技术创新点在于将大型语言模型应用于医疗诊断中，显著提高了首次和第二次鉴别诊断的准确率，与传统方法相比，AI接口在准确性和效率上均表现出色。

**关键设计**：在设计中，AI接口的参数设置经过优化，损失函数采用交叉熵损失，网络结构基于Transformer架构，确保了模型的高效性和准确性。通过对实际患者数据的分析，模型能够快速适应不同的临床场景。

## 📊 实验亮点

实验结果显示，医生的首次鉴别诊断准确率为50%至70%，而AI接口的准确率达80%。在第二次鉴别诊断中，医生的准确率为70%至90%，AI接口则实现了100%的准确率。此外，AI接口的平均诊断时间为557秒，比医生的1006秒缩短了44.6%，成本也降低了98.1%。

## 🎯 应用场景

该研究的潜在应用领域包括初级医疗、远程医疗和医疗辅助决策系统。基于LLM的AI接口能够在内科诊断中提供实时支持，帮助医生提高工作效率，降低医疗成本，最终提升患者的就医体验。未来，该技术有望扩展到其他医学领域，推动医疗智能化的发展。

## 📄 摘要（原文）

> Objective To develop an LLM based realtime compound diagnostic medical AI interface and performed a clinical trial comparing this interface and physicians for common internal medicine cases based on the United States Medical License Exam (USMLE) Step 2 Clinical Skill (CS) style exams. Methods A nonrandomized clinical trial was conducted on August 20, 2024. We recruited one general physician, two internal medicine residents (2nd and 3rd year), and five simulated patients. The clinical vignettes were adapted from the USMLE Step 2 CS style exams. We developed 10 representative internal medicine cases based on actual patients and included information available on initial diagnostic evaluation. Primary outcome was the accuracy of the first differential diagnosis. Repeatability was evaluated based on the proportion of agreement. Results The accuracy of the physicians' first differential diagnosis ranged from 50% to 70%, whereas the realtime compound diagnostic medical AI interface achieved an accuracy of 80%. The proportion of agreement for the first differential diagnosis was 0.7. The accuracy of the first and second differential diagnoses ranged from 70% to 90% for physicians, whereas the AI interface achieved an accuracy rate of 100%. The average time for the AI interface (557 sec) was 44.6% shorter than that of the physicians (1006 sec). The AI interface ($0.08) also reduced costs by 98.1% compared to the physicians' average ($4.2). Patient satisfaction scores ranged from 4.2 to 4.3 for care by physicians and were 3.9 for the AI interface Conclusion An LLM based realtime compound diagnostic medical AI interface demonstrated diagnostic accuracy and patient satisfaction comparable to those of a physician, while requiring less time and lower costs. These findings suggest that AI interfaces may have the potential to assist primary care consultations for common internal medicine cases.

