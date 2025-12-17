---
layout: default
title: Generating Findings for Jaw Cysts in Dental Panoramic Radiographs Using GPT-4o: Building a Two-Stage Self-Correction Loop with Structured Output (SLSO) Framework
---

# Generating Findings for Jaw Cysts in Dental Panoramic Radiographs Using GPT-4o: Building a Two-Stage Self-Correction Loop with Structured Output (SLSO) Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02001" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02001v2</a>
  <a href="https://arxiv.org/pdf/2510.02001.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02001v2" onclick="toggleFavorite(this, '2510.02001v2', 'Generating Findings for Jaw Cysts in Dental Panoramic Radiographs Using GPT-4o: Building a Two-Stage Self-Correction Loop with Structured Output (SLSO) Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nanaka Hosokawa, Ryo Takahashi, Tomoya Kitano, Yukihiro Iida, Chisako Muramatsu, Tatsuro Hayashi, Yuta Seino, Xiangrong Zhou, Takeshi Hara, Akitoshi Katsumata, Hiroshi Fujita

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-02 (更新: 2025-10-06)

**备注**: Submitted to Scientific Reports

---

## 💡 一句话要点

**利用GPT-4o和SLSO框架自动生成牙科全景片中颌骨囊肿的诊断结果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GPT-4o` `颌骨囊肿` `牙科全景片` `自动诊断` `自校正循环` `结构化输出` `多模态学习`

## 📋 核心要点

1. 现有方法在牙科全景片颌骨囊肿诊断中存在准确率不足、易产生幻觉等问题，限制了其临床应用。
2. 论文提出基于GPT-4o和结构化输出自校正循环（SLSO）框架的方法，迭代优化诊断结果，提高准确性和一致性。
3. 实验结果表明，SLSO框架在牙齿编号、牙齿移动和牙根吸收等方面的诊断准确率有显著提升，有效抑制了幻觉。

## 📝 摘要（中文）

本研究利用OpenAI GPT-4o的多模态能力，自动生成牙科全景片中颌骨囊肿的诊断结果。为了提高准确性，构建了一个基于结构化输出的自校正循环（SLSO）框架，并验证了其有效性。针对22例颌骨囊肿病例，实施了一个包含10个步骤的过程，包括图像输入和分析、结构化数据生成、牙齿编号提取和一致性检查、检测到不一致时进行迭代再生，以及生成诊断结果并进行后续重构和一致性验证。通过七个评估项目（透明度、内部结构、边界、牙根吸收、牙齿移动、与其他结构的关系和牙齿编号）与传统的思维链（CoT）方法进行了比较实验。结果表明，所提出的SLSO框架提高了许多项目的输出准确性，牙齿编号、牙齿移动和牙根吸收的改进率分别为66.9%、33.3%和28.6%。在成功的案例中，经过最多五次再生后，实现了持续的结构化输出。尽管由于数据集较小而未达到统计学意义，但总体SLSO框架强制执行了阴性发现描述，抑制了幻觉，并提高了牙齿编号识别的准确性。然而，准确识别跨越多个牙齿的广泛病变是有限的。尽管如此，仍需要进一步改进以提高整体性能，并朝着实用的诊断结果生成系统迈进。

## 🔬 方法详解

**问题定义**：论文旨在解决牙科全景片中颌骨囊肿的自动诊断问题。现有方法，如直接使用大型语言模型（LLM），容易产生幻觉，且输出结果缺乏结构化，难以保证诊断的准确性和一致性。尤其是在牙齿编号、病灶范围等细节信息的识别上，现有方法存在明显不足。

**核心思路**：论文的核心思路是利用GPT-4o的多模态能力，结合结构化输出和自校正循环，迭代优化诊断结果。通过将诊断过程分解为多个步骤，并引入一致性检查机制，可以有效减少幻觉，提高诊断的准确性和可靠性。结构化输出保证了结果的可解释性和可追溯性。

**技术框架**：整体框架是一个两阶段的自校正循环（SLSO）。第一阶段是初始诊断生成阶段，包括图像输入、图像分析、结构化数据生成和牙齿编号提取。第二阶段是自校正阶段，包括一致性检查、迭代再生和结果重构。如果检测到不一致，系统会进行迭代再生，直到满足一致性要求。最终输出结构化的诊断结果。

**关键创新**：最重要的创新点在于SLSO框架的设计。该框架通过结构化输出和自校正循环，有效提升了LLM在医学图像诊断中的可靠性和准确性。与传统的思维链（CoT）方法相比，SLSO框架能够更好地控制LLM的输出，减少幻觉，并提高细节信息的识别准确率。

**关键设计**：SLSO框架的关键设计包括：1) 10步诊断流程的细致分解；2) 结构化数据输出格式的定义，包括透明度、内部结构、边界、牙根吸收、牙齿移动、与其他结构的关系和牙齿编号等关键信息；3) 一致性检查规则的制定，例如牙齿编号的有效性检查；4) 迭代再生的触发机制，当检测到不一致时，系统会自动触发再生过程，直至满足一致性要求。

## 📊 实验亮点

实验结果表明，SLSO框架在牙齿编号、牙齿移动和牙根吸收等方面的诊断准确率分别提高了66.9%、33.3%和28.6%。虽然由于数据集较小，统计学意义不显著，但SLSO框架有效抑制了幻觉，并强制执行了阴性发现描述，证明了其在提高诊断准确性和可靠性方面的潜力。

## 🎯 应用场景

该研究成果可应用于辅助牙科医生进行颌骨囊肿的诊断，提高诊断效率和准确性，尤其是在缺乏经验的医生或资源有限的地区。未来，该系统可以集成到牙科影像分析软件中，实现自动化的诊断报告生成，并为患者提供更快速、更可靠的诊断结果。

## 📄 摘要（原文）

> In this study, we utilized the multimodal capabilities of OpenAI GPT-4o to automatically generate jaw cyst findings on dental panoramic radiographs. To improve accuracy, we constructed a Self-correction Loop with Structured Output (SLSO) framework and verified its effectiveness. A 10-step process was implemented for 22 cases of jaw cysts, including image input and analysis, structured data generation, tooth number extraction and consistency checking, iterative regeneration when inconsistencies were detected, and finding generation with subsequent restructuring and consistency verification. A comparative experiment was conducted using the conventional Chain-of-Thought (CoT) method across seven evaluation items: transparency, internal structure, borders, root resorption, tooth movement, relationships with other structures, and tooth number. The results showed that the proposed SLSO framework improved output accuracy for many items, with 66.9%, 33.3%, and 28.6% improvement rates for tooth number, tooth movement, and root resorption, respectively. In the successful cases, a consistently structured output was achieved after up to five regenerations. Although statistical significance was not reached because of the small size of the dataset, the overall SLSO framework enforced negative finding descriptions, suppressed hallucinations, and improved tooth number identification accuracy. However, the accurate identification of extensive lesions spanning multiple teeth is limited. Nevertheless, further refinement is required to enhance overall performance and move toward a practical finding generation system.

