---
layout: default
title: "Longitudinal and Multimodal Recording System to Capture Real-World Patient-Clinician Conversations for AI and Encounter Research: Protocol"
---

# Longitudinal and Multimodal Recording System to Capture Real-World Patient-Clinician Conversations for AI and Encounter Research: Protocol

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16378" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16378v2</a>
  <a href="https://arxiv.org/pdf/2509.16378.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16378v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16378v2', 'Longitudinal and Multimodal Recording System to Capture Real-World Patient-Clinician Conversations for AI and Encounter Research: Protocol')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Misk Al Zahidy, Kerly Guevara Maldonado, Luis Vilatuna Andrango, Ana Cristina Proano, Ana Gabriela Claros, Maria Lizarazo Jimenez, David Toro-Tobon, Victor M. Montori, Oscar J. Ponce-Ponte, Juan P. Brito

**分类**: cs.CY, cs.CL

**发布日期**: 2025-09-19 (更新: 2025-09-26)

**备注**: 23 pages, 2 figures, 2 tables

---

## 💡 一句话要点

**构建纵向多模态记录系统，捕捉真实医患对话，促进AI与诊疗研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医患互动` `多模态数据` `人工智能` `临床诊疗` `电子健康记录`

## 📋 核心要点

1. 现有AI模型主要依赖EHR数据，缺乏对医患互动信息的捕捉，导致AI系统可能存在片面性。
2. 本研究设计并实施一个纵向多模态系统，整合360度视频/音频、调查问卷和EHR数据，全面记录医患互动。
3. 研究结果显示，临床医生和患者的同意率较高，记录和调查完成率良好，证明了该框架的可行性。

## 📝 摘要（中文）

医学人工智能的潜力取决于从反映患者和临床医生需求的数据中学习。现有模型主要基于电子健康记录（EHR）训练，这些记录捕捉生物学指标，但很少包含医患互动。医患关系是医疗的核心，体现在语音、文本和视频中，但现有数据集缺乏这些信息。因此，仅基于EHR训练的AI系统可能延续狭隘的生物医学视角，忽略定义临床诊疗过程的真实交流。本研究旨在设计、实施和评估一个纵向多模态系统，用于捕捉医患互动，将360度视频/音频记录与调查和EHR数据关联，从而创建一个用于AI研究的数据集。该单中心研究在梅奥诊所的内分泌科门诊进行。招募参与临床医生的成年患者。使用360度摄像机记录诊疗过程。每次就诊后，患者完成关于共情、满意度、节奏和治疗负担的调查。从EHR中提取人口统计学和临床数据。可行性评估使用五个指标：临床医生同意率、患者同意率、记录成功率、调查完成率以及跨模态数据链接。招募工作于2025年1月开始。截至2025年8月，36名符合条件的临床医生中有35名（97%）和281名受邀患者中有212名（75%）表示同意。在同意记录的诊疗中，162次（76%）有完整记录，204次（96%）完成了调查。本研究旨在展示一个可复制框架的可行性，用于捕捉医患互动的多模态动态。通过详细说明工作流程、指标和伦理保障，它为纵向数据集提供了一个模板，并为包含复杂医疗信息的AI模型奠定了基础。

## 🔬 方法详解

**问题定义**：现有医学AI模型主要依赖电子健康记录(EHR)数据进行训练，这些数据虽然包含了患者的生物学指标，但缺乏对医患之间互动交流的记录。这种缺失导致AI模型难以理解医疗过程中的复杂性和细微差别，例如患者的情感、医生的沟通方式以及双方的互动模式。因此，如何有效地捕捉和利用医患互动信息，成为了提升医学AI模型性能的关键问题。

**核心思路**：本研究的核心思路是构建一个纵向、多模态的数据采集系统，全面记录医患互动的各个方面。通过整合360度视频/音频记录、患者调查问卷和电子健康记录数据，创建一个包含语音、文本、视频和结构化数据的综合数据集。这种多模态的数据融合能够更完整地呈现医患互动的全貌，为AI模型提供更丰富的学习素材。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 招募参与研究的临床医生和患者；2) 在诊室安装360度摄像机，用于记录医患互动的全过程；3) 在每次就诊后，患者填写调查问卷，评估医生共情能力、患者满意度、诊疗节奏和治疗负担；4) 从电子健康记录中提取患者的人口统计学和临床数据；5) 将不同模态的数据进行链接和整合，形成一个完整的医患互动数据集。

**关键创新**：本研究的关键创新在于其纵向、多模态的数据采集方法。与以往主要依赖EHR数据的研究不同，该研究通过整合视频、音频、文本和结构化数据，全面记录医患互动的各个方面。这种多模态的数据融合能够更完整地呈现医患互动的全貌，为AI模型提供更丰富的学习素材。此外，该研究还注重数据的伦理性和安全性，采取了严格的隐私保护措施。

**关键设计**：在数据采集过程中，研究人员选择了360度摄像机，以确保能够捕捉到诊室内的所有细节。在调查问卷的设计上，研究人员选择了经过验证的量表，以确保数据的可靠性和有效性。在数据链接方面，研究人员采用了唯一标识符，将不同模态的数据进行关联。此外，研究人员还制定了详细的数据管理和存储方案，以确保数据的安全性和可访问性。

## 📊 实验亮点

研究结果显示，临床医生同意率高达97%，患者同意率为75%，表明该研究方法具有良好的接受度。在同意记录的诊疗中，76%有完整记录，96%完成了调查，证明了数据采集的可行性。这些数据表明，该研究构建的多模态数据采集系统能够有效地捕捉医患互动信息，为后续的AI研究奠定了坚实的基础。

## 🎯 应用场景

该研究成果可应用于开发更智能的医疗AI系统，例如辅助诊断、个性化治疗方案推荐、医患沟通技巧培训等。通过分析医患互动数据，可以识别影响治疗效果的关键因素，从而优化医疗服务流程，提升患者满意度和治疗效果。此外，该数据集还可以用于研究医患关系、医疗决策过程等，为医学研究提供新的视角。

## 📄 摘要（原文）

> The promise of AI in medicine depends on learning from data that reflect what matters to patients and clinicians. Most existing models are trained on electronic health records (EHRs), which capture biological measures but rarely patient-clinician interactions. These relationships, central to care, unfold across voice, text, and video, yet remain absent from datasets. As a result, AI systems trained solely on EHRs risk perpetuating a narrow biomedical view of medicine and overlooking the lived exchanges that define clinical encounters. Our objective is to design, implement, and evaluate the feasibility of a longitudinal, multimodal system for capturing patient-clinician encounters, linking 360 degree video/audio recordings with surveys and EHR data to create a dataset for AI research. This single site study is in an academic outpatient endocrinology clinic at Mayo Clinic. Adult patients with in-person visits to participating clinicians are invited to enroll. Encounters are recorded with a 360 degree video camera. After each visit, patients complete a survey on empathy, satisfaction, pace, and treatment burden. Demographic and clinical data are extracted from the EHR. Feasibility is assessed using five endpoints: clinician consent, patient consent, recording success, survey completion, and data linkage across modalities. Recruitment began in January 2025. By August 2025, 35 of 36 eligible clinicians (97%) and 212 of 281 approached patients (75%) had consented. Of consented encounters, 162 (76%) had complete recordings and 204 (96%) completed the survey. This study aims to demonstrate the feasibility of a replicable framework for capturing the multimodal dynamics of patient-clinician encounters. By detailing workflows, endpoints, and ethical safeguards, it provides a template for longitudinal datasets and lays the foundation for AI models that incorporate the complexity of care.

