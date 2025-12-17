---
layout: default
title: AnySleep: a channel-agnostic deep learning system for high-resolution sleep staging in multi-center cohorts
---

# AnySleep: a channel-agnostic deep learning system for high-resolution sleep staging in multi-center cohorts

**arXiv**: [2512.14461v1](https://arxiv.org/abs/2512.14461) | [PDF](https://arxiv.org/pdf/2512.14461.pdf)

**作者**: Niklas Grieger, Jannik Raskob, Siamak Mehrkanoon, Stephan Bialonski

**分类**: cs.LG, eess.SP, q-bio.QM

**发布日期**: 2025-12-16

**备注**: 18 pages, 6 figures, 2 tables

---

## 💡 一句话要点

**提出AnySleep深度学习系统，以解决多中心睡眠研究中电极设置异质性和时间分辨率固定的问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `睡眠分期` `深度学习` `脑电图分析` `多中心研究` `时间分辨率可调` `通道无关模型` `生物标志物发现` `睡眠障碍诊断`

## 📋 核心要点

1. 核心问题：传统睡眠分期依赖人工评分，电极设置和时间分辨率（30秒）固定，限制了多中心研究和短时生物标志物发现。
2. 方法要点：开发AnySleep深度学习模型，利用任意EEG或EOG数据，支持可调时间分辨率，实现跨中心稳健泛化。
3. 实验或效果：在21个数据集上验证，性能达SOTA，在30秒以下尺度捕获短时觉醒，提升生理和病理预测能力。

## 📝 摘要（中文）

睡眠对健康至关重要，但研究其动态需要人工睡眠分期，这是睡眠研究和临床护理中劳动密集的步骤。传统上，多导睡眠图（PSG）记录在30秒时段内评分，这是出于实用而非生理原因，且电极数量、导联方式和受试者特征差异很大。这些限制给开展协调的多中心睡眠研究以及在更短时间尺度上发现新的、稳健的生物标志物带来了挑战。本文提出AnySleep，一种深度神经网络模型，可使用任何脑电图（EEG）或眼电图（EOG）数据以可调时间分辨率进行睡眠评分。我们在来自21个数据集的超过19,000个夜间记录上训练和验证了该模型，涵盖近200,000小时的EEG和EOG数据，以促进跨站点的稳健泛化。该模型达到了最先进的性能，在30秒时段上超越或等同于现有基线。提供更多通道时性能提高，但当EOG缺失或仅EOG或单个EEG导联（额叶、中央或枕叶）可用时，性能仍然强劲。在30秒以下的时间尺度上，该模型捕获了与觉醒一致的短暂清醒侵入，并相对于标准的30秒评分，改善了生理特征（年龄、性别）和病理生理状况（睡眠呼吸暂停）的预测。我们公开提供该模型，以促进具有异质电极设置的大规模研究，并加速睡眠中新生物标志物的发现。

## 🔬 方法详解

AnySleep是一个深度神经网络模型，整体框架基于深度学习处理EEG和EOG信号。关键技术创新点包括：通道无关设计，能处理任意电极数量和导联方式；支持可调时间分辨率，突破传统30秒限制；利用大规模多中心数据（19,000+记录）训练，增强泛化能力。与现有方法的主要区别在于其灵活性和高分辨率能力，传统方法通常固定于特定电极设置和30秒时段，而AnySleep适应异质设置并支持更细粒度分析。

## 📊 实验亮点

模型在30秒时段达到SOTA性能，超越基线；在30秒以下尺度捕获短时觉醒，提升年龄、性别和睡眠呼吸暂停预测；即使仅用单通道EEG或EOG，性能仍强劲。

## 🎯 应用场景

该研究可应用于多中心睡眠研究、临床睡眠监测和生物标志物发现。实际价值在于促进大规模协调研究，加速新睡眠障碍诊断工具开发，并支持个性化医疗。

## 📄 摘要（原文）

> Sleep is essential for good health throughout our lives, yet studying its dynamics requires manual sleep staging, a labor-intensive step in sleep research and clinical care. Across centers, polysomnography (PSG) recordings are traditionally scored in 30-s epochs for pragmatic, not physiological, reasons and can vary considerably in electrode count, montage, and subject characteristics. These constraints present challenges in conducting harmonized multi-center sleep studies and discovering novel, robust biomarkers on shorter timescales. Here, we present AnySleep, a deep neural network model that uses any electroencephalography (EEG) or electrooculography (EOG) data to score sleep at adjustable temporal resolutions. We trained and validated the model on over 19,000 overnight recordings from 21 datasets collected across multiple clinics, spanning nearly 200,000 hours of EEG and EOG data, to promote robust generalization across sites. The model attains state-of-the-art performance and surpasses or equals established baselines at 30-s epochs. Performance improves as more channels are provided, yet remains strong when EOG is absent or when only EOG or single EEG derivations (frontal, central, or occipital) are available. On sub-30-s timescales, the model captures short wake intrusions consistent with arousals and improves prediction of physiological characteristics (age, sex) and pathophysiological conditions (sleep apnea), relative to standard 30-s scoring. We make the model publicly available to facilitate large-scale studies with heterogeneous electrode setups and to accelerate the discovery of novel biomarkers in sleep.

